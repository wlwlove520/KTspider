#!/usr/bin/env python
# -- coding: utf-8 --
import json
import aiohttp
import asyncio
import requests
import logging
from asyncio import Queue

from spider.save_result import SaverAsync
from config import *

logging.basicConfig(filename='logger.log', level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(filename)s "%(message)s"',
                    datefmt='[%d/%b/%Y %H:%M:%S]',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)




class Fetcher(object):
    def __init__(self, t):
        self.t = t
        self._session = None
        self._loop = asyncio.get_event_loop()
        self.headers = get_header()
        self._newq = Queue(loop=self._loop)
        self.save = SaverAsync()
        self.put_task(t.task)

        self.proxy_url = 'http://127.0.0.1:8000/?types=0&count=10&country=国内'
        self.change_proxy = False


    def delete_ip(self, ip):
        r = requests.get('http://127.0.0.1:8000/delete?ip=%s' % ip)
        logging.info('delete ip is: %s', r)

    def get_proxies(self):
        """
        get proxies
        :return:
        """
        try:
            r = requests.get(self.proxy_url)
            ip_ports = json.loads(r.content.decode('ascii'))
            import random
            size = random.randint(0, len(ip_ports) - 1)
            ip_ports_random = ip_ports[size]
            ip = ip_ports_random[0]
            port = ip_ports_random[1]
            # proxies = {
            #     'http': 'http://%s:%s' % (ip, port),
            #     'https': 'http://%s:%s' % (ip, port)
            # }
            proxies = 'http://%s:%s' % (ip, port)
            return proxies, ip
        except Exception as e:
            logging.error('change proxy error: %s', e)
            return '', ''

    def init_session(self):
        """
        initial self._session
        :return:
        """
        if not self._session:
            self._session = aiohttp.ClientSession(loop=self._loop,headers=self.headers)

    async def close_session(self):
        """
        close self._session
        :return:
        """
        if not self._session.closed:
            await self._session.close()

    async def get_response(self, url,request_type,datas):
        """
        get response.text()
        :param url:
        :return:
        """
        try:
            self.headers = get_header()
            if self.change_proxy:
                proxy, ip = self.get_proxies()
                logging.info('get proxy: %s' % proxy)
                self.change_proxy = False
                async with self._session.get(url, headers=self.headers, proxy=proxy) as response:
                    assert response.status == 200
                    return await response.text()
            if request_type == 'post':
                async with self._session.post(url, headers=self.headers, data = datas) as response:
                    # assert response.status == 200
                    try:
                        return await response.text()
                    except:
                        try:
                            return await response.text(encoding='gbk')
                        except:
                            try:
                                return await response.text(encoding='gb18030')
                            except:
                                return await response.text(encoding='gb18030', errors='ignore')
            else:
                async with self._session.get(url, headers=self.headers) as response:
                    # assert response.status == 200
                    try:
                        return await response.text()
                    except:
                        try:
                            return await response.text(encoding='gbk')
                        except:
                            try:
                                return await response.text(encoding='gb18030')
                            except:
                                return await response.text(encoding='gb18030', errors='ignore')
        except TimeoutError as e:
            logging.error('get html timeout:%s', e)
            return ''
        # except Exception as e:
        #     return

    async def get_a_task(self):
        """
        get a task
        :return:
        """
        task_content = await self._newq.get()
        if not task_content:
            return None
        # return eval(task_content)
        return task_content

    def finish_a_task(self):
        """
        finish a task
        :return:
        """
        self._newq.task_done()

    def put_task(self, _t):
        """
        :param _t:
        :return:
        """

        def task_parse(tt):
            for url in tt.get('url'):
                info_d = dict()
                for key in tt.keys():
                    info_d[key] = tt.get(key)
                info_d['url'] = url
                yield info_d

        while True:
            try:
                _task = next(_t)
                _task = task_parse(_task)
                for x in _task:
                    self._newq.put_nowait(x)
            except StopIteration:
                break

    async def get_content(self, index):
        """
        fetcher(main)
        :return:
        """
        # logging.warning("%s[worker-%s] start...", self.__class__.__name__, index)
        while True:
            try:
                if self._newq.qsize() == 0:
                    break
                task = await self.get_a_task()
                url = task.get('url')
                request_type = task.get('request_type','')
                datas = task.get('datas','')
                print(url)

                content = await self.get_response(url,request_type,datas)

                # if content:
                #     continue
                resp_content, new = await self.t.process_result(task, content)
                save_result = await self.save.save(url, resp_content)
                if save_result:
                    pass  # 判断抓取进度
                if new:
                    self.put_task(new)

                self.finish_a_task()
            except asyncio.CancelledError as e:
                self.finish_a_task()
                logging.error("%s [worker-%s] error: %s", self.__class__.__name__, index, e)
            except AssertionError as e:
                self.finish_a_task()
                logging.error("response is not 200, url: %s", e)
            except Exception as e:
                # task['retry'] += 1
                # if task['retry'] <= 3:
                #     self._newq.put_nowait(task)
                self.finish_a_task()
                logging.error("%s [worker-%s] error: %s", self.__class__.__name__, index, e)

            # finally:
            #     self.finish_a_task()

    async def _start(self, fetcher_num):
        """
        start the fetcher
        :return:
        """
        self.init_session()
        tasks_list = [asyncio.Task(self.get_content(index + 1), loop=self._loop) for index in range(fetcher_num)]
        await self._newq.join()
        for task in tasks_list:
            task.cancel()

    def start(self, fetcher_num=10):
        try:

            self._loop.run_until_complete(self._start(fetcher_num))
        except Exception as e:
            logging.error("%s start_work_and_wait_done error:" % self.__class__.__name__, e)
        finally:
            # self.save.close_producer()
            # self.close_session()
            self._loop.run_until_complete(self.close_session())
            self._loop.stop()
            self._loop.run_forever()
            self._loop.close()
            self.save.close_db_and_conn()
