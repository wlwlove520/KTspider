#!/usr/bin/python
# coding:utf-8
import urllib.request as ub, socket
import sys
import os
import time
import threading
from KTqueue import bloom_filter as SQqueue
import logging
import oss2
import requests

hds = {'User-Agent': 'chrome/28.0.1500.72', }
date_n = time.strftime("%Y%m", time.localtime(time.time()))


# proxy_h=urllib2.ProxyHandler({'http':'http://127.0.0.1:8087'})
# opener=urllib2.build_opener(proxy_h)
# urllib2.install_opener(opener)

class getImgThread(threading.Thread):
    def __init__(self, imgsrc, fname, oss_path, mutex):
        threading.Thread.__init__(self)
        self.url = imgsrc
        self.fileName = fname
        self.mutex = mutex
        self.oss_path = oss_path
        self.auth = oss2.Auth('osskey', 'aaaaaa')
        self.bucket = oss2.Bucket(self.auth, 'oss path', 'oss bucket')

    def schedule(self, a, b, c):
        per = a * b / c
        if per >= 1:
            logging.info("down img src=%s", self.url)

    def put_img(self):
        try:
            resp_img = requests.get(self.url, timeout=5)
            result = self.bucket.put_object(self.oss_path, resp_img)
            logging.info("put img to oss [status]:{0}  [request_id]:{1}".format(result.status, result.request_id))
        except Exception as e:
            logging.error("put img error: %s", e)

    def run(self):
        self.mutex.acquire()
        self.mutex.release()
        try:
            # ub.urlretrieve(self.url, self.fileName, self.schedule)
            self.put_img()
        except IOError:
            time.sleep(1)


def down_img():
    socket.setdefaulttimeout(10)
    try:
        os.mkdir(date_n)
    except OSError as e:
        if e.errno == 17:  # 如果是文件已经存在，则不做任何操作
            pass
        else:  # 如果是其他异常，则打印出异常，并退出程序
            logging.error('down img error: %s', e)
            sys.exit()
    os.chdir(date_n)
    q = SQqueue.Queue('KT_img')
    mutex = threading.Lock()
    while True:
        URL = q.get()
        if not URL:
            continue
        try:
            img_url = URL.decode()
            file_name = img_url.split('/')[-1]  # 取文件名
            oss_path = 'img/' + str(date_n) + '/' + file_name
            t = getImgThread(img_url, file_name, oss_path, mutex)
            t.start()
        except Exception as e:
            logging.error('get img class error: %s', e)


if __name__ == '__main__':
    down_img()
