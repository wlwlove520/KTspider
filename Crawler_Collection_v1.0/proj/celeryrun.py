# -*-coding:utf-8-*-
from celery import Celery
import configparser


class Cel:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('/home/linhanqiu/crawler240/proj/conf.ini')
        self.broker = self.conf.get("baseconf","broker")
        self.backend = self.conf.get("baseconf","backend")
    def __call__(self, *args, **kwargs):
        app = Celery('proj',
                     broker=self.broker,
                     backend=self.backend,
                     include=['proj.tasks'])
        app.conf.update(
            result_expires=3600,
        )
        return app


test = Cel()
app = test()
app.start()