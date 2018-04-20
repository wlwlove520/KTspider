#!/usr/bin/python
# coding:utf-8
import time
import logging
import sys
from io import BytesIO
import logging.handlers
import json

sys.path.append('/home/obs_img_project/SQspider')

import requests

from my_obs_client.obs_client import ObsClient
from KTqueue import bloom_filter as SQqueue
from config import *

hds = {'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）',
       'Connection': 'keep-alive'}

logger = logging.getLogger()
# LOG_FILE = "/home/obs_img_project/logs/error.log"
# hdlr = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='D', interval=1, backupCount=40)
formatter = logging.Formatter('%(levelname)s: %(asctime)s %(filename)s "%(message)s', datefmt='[%d/%b/%Y %H:%M:%S]')
# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


class getImgThread(object):
    def __init__(self, url, date_n):
        self.retry = 0
        self.date = str(date_n)
        self.connect = ObsClient(AK, SK, is_secure=True, server=SERVER, signature=SIGNATURE, region=REGION,
                                 path_style=True, timeout=5)
        self.url = url
        # self.oss_path = oss_path
        # self.auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        # self.bucket = oss2.Bucket(self.auth, OSS_HOST, OSS_BUCKET)

    def put_img(self, url, obs_path):
        try:
            resp_img = requests.get(url, timeout=10)
            result = self.connect.putContent(BUCKET_NAME, obs_path, BytesIO(resp_img.content))
            print(result)
            status = json.loads(json.dumps(result)).get('status')
            if status == 200:
                logging.info("put img to obs [status]:{0}  [request_id]:{1}".format(result.status, result.request_id))
        except Exception as e:
            import traceback
            print(traceback.print_exc(e))
            time.sleep(1)

    def run(self):
        # img_url = self.url.decode()
        img_url = self.url
        if '\x01' in img_url:
            self.retry, img_url = img_url.split('\x01')
            if self.retry > 3:
                logging.warning("get img error: {url}".format(url=img_url))
                return
        file_name = img_url.split('/')[-1]  # 取文件名
        if img_url.split('/')[-1] == '641.jpg':
            file_name = img_url.split('/')[-2] + img_url.split('/')[-1]
        elif img_url.split('/')[-1] == '0.jpg':
            file_name = img_url.split('/')[-2] + img_url.split('/')[-1]
        elif img_url.split('/')[-1] == '1024.jpg':
            file_name = img_url.split('/')[-2] + img_url.split('/')[-1]
        obs_path = 'img/' + self.date + '/' + file_name
        self.put_img(img_url, obs_path)


def down_img():
    q = SQqueue.Queue(QUEUE_IMG_NAME_ERROR)
    all_url = ['http://pic.enorth.com.cn/004/052/459/00405245962_2d700d03.jpg',
               'http://pic.enorth.com.cn/004/056/164/00405616409_0fba988a.jpg',
               'http://pic.enorth.com.cn/004/055/295/00405529524_16f61f41.jpg',
               'http://sh.eastday.com/images/thumbnailimg/month_1712/ba0b104f4d88491cb1127687421d425c.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/27/20171227171446139.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/27/20171227171525217.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/27/20171227171548498.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/27/20171227171532131.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/27/2017122717150669.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/27/2017122716139310.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/27/20171227161359160.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/28/201712288519508.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/28/2017122894243641.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/28/2017122894151112.jpg',
               'http://Pic.66wc.com/pic/news_edit/2017/12/28/201712289423238.jpg',
               'https://wx3.sinaimg.cn/large/0005c673gy3feal5mue2ej20sg0sgb29.jpg',
               'https://wx3.sinaimg.cn/large/0005c673gy3feal61v8ahj211y0sg4qq.jpg',
               'https://wx3.sinaimg.cn/large/0001c720gy3fema9gqphkj20m80goe3c.jpg',
               'http://s3img.city.sina.com.cn/xiancheng/common/thumbnail/0/deee2c6808b08500039bfd736ab88d5d.jpg',
               'http://static.52liaoshen.com/Uploads/201712/28/a6f0edc2f9485d1b.jpg',
               'http://static.52liaoshen.com/Uploads/201712/28/11b0f98cb53adb9f.jpg',
               'http://static.52liaoshen.com/Uploads/201712/28/57ecee0f2120122f.jpg',
               'http://static.52liaoshen.com/Uploads/201712/28/001d97b5d6277e0c.jpg',
               'http://www.qhnews.com/pic/0/01/43/71/1437176_511780.jpg',
               'http://www.qhnews.com/pic/0/01/43/71/1437183_178595.jpg',
               'http://www.qhnews.com/pic/0/01/43/71/1437185_820356.jpg',
               'http://www.qhnews.com/pic/0/01/43/71/1437186_037956.jpg',
               'http://www.qhnews.com/pic/0/01/43/71/1437187_861372.jpg',
               'http://www.qhnews.com/pic/0/01/43/71/1437132_526908.jpg',
               'http://www.qhnews.com/pic/0/01/43/69/1436982_239148.jpg',
               'http://www.qhnews.com/pic/0/01/43/69/1436988_041684.png',
               'http://www.qhnews.com/pic/0/01/43/71/1437119_835250.jpg',
               'http://www.qhnews.com/pic/0/01/43/72/1437238_979729.jpg',
               'http://www.qhnews.com/pic/0/01/43/72/1437240_589864.jpg',
               'http://www.qhnews.com/pic/0/01/43/69/1436953_465480.jpg',
               'http://www.qhnews.com/pic/0/01/43/69/1436940_794271.jpg',
               'http://www.qhnews.com/pic/0/01/43/71/1437133_430494.jpg',
               'http://www.dlxww.com/news/content/images/attachement/jpg/site102/20171226/002197282ec31bab6e7b21.jpg',
               'http://www.jz.gov.cn/jzszf/jzzc61/jrjz/4338000/1.jpg',
               'http://www.jz.gov.cn/jzszf/jzzc61/jrjz/4338000/F19W071100.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_201712289501722058.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_201712289504548706.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_20171228951234672.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_201712289512997512.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_201712289513946372.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_201712289515049097.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_201712289515274139.jpg',
               'http://www.zsnews.cn/data/photo/Backup/2017/12/28/tw_201712289462540673.jpg',
               'http://www.dlxww.com/news/content/images/attachement/jpg/site102/20171226/A041514218815488_change_A04C26-1b001.jpg',
               'http://www.dlxww.com/news/content/images/attachement/jpg/site102/20171228/A031514392796238_change_guqp171242_b.jpg',
               'http://www.jz.gov.cn/jzszf/jzzc61/jrjz/4339484/2017122509410251609.jpg',
               'http://www.jz.gov.cn/jzszf/jzzc61/jrjz/4339484/2017122509411362343.jpg',
               'http://www.jz.gov.cn/jzszf/jzzc61/jrjz/4339484/2017122509412833761.jpg',
               'http://www.jz.gov.cn/jzszf/jzzc61/jrjz/4339484/2017122509415168599.jpg',
               'http://www.jz.gov.cn/jzszf/jzzc61/jrjz/4339484/2017122509414063530.jpg',
               'http://www.gywb.cn/xinwen/attachement/jpg/site2/20171226/ac220b83a0f61bac4f6408.jpg',
               'http://www.gywb.cn/xinwen/attachement/jpg/site2/20171226/ac220b83a0f61bac4f6f09.jpg',
               'http://www.gywb.cn/xinwen/attachement/jpg/site2/20171226/3417eb9bc7b41babec8c02.jpg',
               'http://xw.kunming.cn/attachement/jpg/site22/20171228/507b9d1afecb1baeaa232e.jpg',
               'http://xw.kunming.cn/attachement/jpg/site22/20171228/6c4b902e0eee1bae8ce61e.jpg',
               'http://dt.push.bz//upload/2017/03/small_news_af9ab63f1b3346e4927e96a3f90694bc.jpg@640w_1l_1c_0i_80q_1x_1e.jpg',
               'http://dt.push.bz//upload/2017/03/small_news_77bf52cdfc904b808a389bf3c5b4c4e2.jpg@640w_1l_1c_0i_80q_1x_1e.jpg',
               'http://dt.push.bz//upload/2017/03/small_news_257fbdbe538447e1b5d0fc69066f96d8.jpg@640w_1l_1c_0i_80q_1x_1e.jpg',
               'http://dt.push.bz/upload/2017/02/0.376047900121681.jpg',
               'http://dt.push.bz/upload/2017/02/0.347785420412098.jpg',
               'http://dt.push.bz/upload/2017/02/0.643383258321967.jpg',
               'http://dt.push.bz/upload/2017/01/0.788095497427553.jpg',
               'http://dt.push.bz/upload/2017/01/0.679130388740045.jpg',
               'http://dt.push.bz/upload/2017/01/0.839448702912521.jpg',
               'http://dt.push.bz/upload/2017/08/0.283963418697921.png']
    for url in all_url:
        date_n = time.strftime("%Y%m", time.localtime(time.time()))
        # url = q.redis_get()
        if not url:
            continue
        d = getImgThread(url, date_n)
        d.run()


if __name__ == '__main__':
    down_img()
