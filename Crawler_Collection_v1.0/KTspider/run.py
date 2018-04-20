# ! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

# from KTqueue import kt_queue as queue
from spider.fetcher import Fetcher
from rules import Rules as r
from spider.script import Task
# from KTimg import crawl_thread_img as cra

sys.path.append(os.getcwd())


def run_in_thread(func, *args, **kwargs):
    """Run function in thread, return a Thread object"""
    from threading import Thread
    thread = Thread(target=func, args=args, kwargs=kwargs)
    thread.daemon = True
    thread.start()
    return thread


def run_in_subprocess(func, *args, **kwargs):
    """Run function in subprocess, return a Process object"""
    from multiprocessing import Process
    thread = Process(target=func, args=args, kwargs=kwargs)
    thread.daemon = True
    thread.start()
    thread.join()
    return thread


def run_fetcher():
    """Run the start function in fetcher"""
    # thread = []
    fetcher = Fetcher(task)
    fetcher.start(fetcher_num=10)


if __name__ == '__main__':
    rules = r.rules_list
    task = Task(rules)
    # q = queue.Queue('kt_queue')
    # for t in task.get_task():
    #     print(t)
    #     q.put_nowait(t)
    # while True:
    #     print(q.get_nowait())
    run_in_subprocess(run_fetcher())
