#!/usr/bin/python
# coding:utf-8
import socket
import time
import threading
import logging
from io import BytesIO
import logging.handlers
import json

# import oss2
# from oss2 import exceptions as ossexception
import requests
from requests import exceptions

from my_obs_client.obs_client import ObsClient
from KTqueue import bloom_filter as SQqueue
from config import *

hds = {'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）',
       'Connection': 'keep-alive'}

logger = logging.getLogger()
LOG_FILE = "/home/obs_img_project/logs/debug.log"
hdlr = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='D', interval=1, backupCount=40)
formatter = logging.Formatter('%(levelname)s: %(asctime)s %(filename)s "%(message)s', datefmt='[%d/%b/%Y %H:%M:%S]')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


class getImgThread(threading.Thread):
    def __init__(self, mutex, my_queue, warn_q, date_n):
        threading.Thread.__init__(self)
        self.img_q = my_queue
        self.wq = warn_q
        self.mutex = mutex
        self.retry = 0
        self.date = str(date_n)
        self.connect = ObsClient(AK, SK, is_secure=True, server=SERVER, signature=SIGNATURE, region=REGION,
                                 path_style=True)
        # self.oss_path = oss_path
        # self.auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        # self.bucket = oss2.Bucket(self.auth, OSS_HOST, OSS_BUCKET)

    def put_img(self, url, obs_path):
        try:
            resp_img = requests.get(url, timeout=10, headers=hds)
            result = self.connect.putContent(BUCKET_NAME, obs_path, BytesIO(resp_img.content))
            status = json.loads(json.dumps(result)).get('status')
            if status == 200:
                logging.info("put img to oss [status]:{0}  [request_id]:{1}".format(result.status, result.request_id))
        except Exception:
            time.sleep(1)
            self.img_q.redis_put(str(self.retry + 1) + '\x01' + url)

    def run(self):
        try:
            self.mutex.acquire()
            url = self.img_q.redis_get()
        finally:
            self.mutex.release()
        # ub.urlretrieve(self.url, self.fileName, self.schedule)
        if not url:
            return
        img_url = url.decode()
        if '\x01' in img_url:
            self.retry, img_url = img_url.split('\x01')
            if self.retry > 3:
                logging.warning("get img error: {url}".format(url=img_url))
                self.wq.redis_put(str(0) + '\x01' + img_url)
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
    socket.setdefaulttimeout(10)
    q = SQqueue.Queue(QUEUE_IMG_NAME)
    warn_queue = SQqueue.Queue(QUEUE_IMG_NAME_WARN)
    mutex = threading.Lock()
    while True:
        date_n = time.strftime("%Y%m", time.localtime(time.time()))
        if threading.activeCount() >= 50:
            continue
        try:
            t = getImgThread(mutex, q, warn_queue, date_n)
            t.start()
        except Exception as e:
            logging.error('get img class error: %s', e)


if __name__ == '__main__':
    down_img()
