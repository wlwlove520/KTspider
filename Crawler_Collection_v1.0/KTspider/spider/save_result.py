#!/usr/bin/env python
# -- coding: utf-8 --
import json
import re
import sys
import logging
import pymysql
from urllib.parse import urljoin

from KTqueue import bloom_filter as SQqueue
from config import *
from tools import filter_file


class SaverAsync(object):
    """
    class of SaverAsync, must include function save()
    """

    def __init__(self, save_pip=sys.stdout):
        self._save_pip = save_pip
        self.t_date = time.strftime("%Y%m", time.localtime(time.time()))
        self.t_date1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.obs_img_path = OBS_IMG_PATH.format(date=str(self.t_date))
        self.img_q = SQqueue.Queue(QUEUE_IMG_NAME)
        self.sql = r"""insert into collection_news (area, category_id, title, news_date, text_f,text, img_show, url_show,classify,languageVersion) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.start_db_and_conn()


    async def save(self, url, result) -> bool:
        """
        save result
        :param url:
        :param result:
        :return: true or false
        """
        if not result:
            save_result = False
            return save_result
        logging.debug("%s start: url=%s", self.__class__.__name__, url)
        try:
            res = json.loads(result)
            # print(res)
            area = deal_area(res.get('area'))
            category_id = res.get('category_id')
            content = res.get('content')
            text_f = res.get('text_f')
            languageVersion = res.get('languageVersion', 'ZH')
            title = ''
            for t in res.get('title'):
                title += t.strip()
            #过滤标题
            title = filter_file.filter_title(area, text_f, title)
            #过滤多余内容
            content = filter_file.filter_cont(area, text_f, content)
            #过滤标签
            content = filter_file.filter_tags(content)


            imgs = re.findall(r'<img.*? src="(.+?)".+?>', content)
            imgs = [i.strip() for i in imgs]
            #替换文章中图片地址
            content = self.replace_img(content, imgs)
            img_show = None
            classify = 0
            if len(imgs) >= 1:  # 大于三张图可以考虑留一下。
                img_show = ','.join([self.obs_img_path + str(src.split('/')[-1]) for src in imgs])
                classify = 2
                if len(imgs) >= 3:
                    classify = 1
                    img_show = ','.join(img_show.split(',')[0:3])
            if imgs:
                for i in imgs:
                    i = urljoin(url, i)
                    self.img_q.redis_put(i)

            # print(content)
            # print(title,news_date,text_f)

            self.save_to_mysql(area, category_id, title, self.t_date1, text_f, content, img_show, url, classify, languageVersion)



            save_result = True
        except IndexError as e:
            save_result = False
            res = json.loads(result)
            logging.error("%s error: %s， area: %s, source: %s",self.__class__.__name__,e,res.get('area'),res.get('text_f'))
        except Exception as e:
            save_result = False
            logging.error("%s error: %s, url=%s",self.__class__.__name__,e,url)

        logging.debug("%s end: save_result=%s, url=%s",self.__class__.__name__,save_result,url)
        return save_result

    def replace_img(self,text, srcs):
        """
        替换内容中的图片路径
        :param text: 文本内容
        :param srcs: 链表形式的图片url
        :return:
        """
        for src in srcs:
            new_path = self.obs_img_path + src.split('/')[-1]
            text = text.replace(src, new_path)
        return text

    def save_to_mysql(self, area, category_id, title, news_date, text_f, content, img_show, url,classify, languageVersion):
        try:
            self.cur.execute(self.sql,(area, category_id, title,news_date, text_f,content, img_show, url,classify, languageVersion))
            logging.info('Save to mysql successful ... %s,%s,%s,%s'%(area,title,news_date,text_f))
            self.db.commit()
        except Exception as e:
            logging.error('Save to mysql error: %s' % e)

    def start_db_and_conn(self):
        try:
            self.db = pymysql.connect(host=HOST_MYSQL, database=DATABASE_MYSQL,
                                      user=USER_MYSQL,
                                      password=PASSWORD_MYSQL, charset=CHARSET_MYSQL)
            self.cur = self.db.cursor()
        except pymysql.err.OperationalError as pymysql_err:
            self.start_db_and_conn()

    def close_db_and_conn(self):
        self.cur.close()
        self.db.close()







if __name__ == '__main__':
    pass
