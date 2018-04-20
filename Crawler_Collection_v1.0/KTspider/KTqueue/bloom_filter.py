#!/usr/bin/env python
# -- coding: utf-8 --
import redis
from hashlib import md5

from config import *


class Queue(object):
    def __init__(self, queue_name, host=HOST, port=PORT):
        self.pool = redis.ConnectionPool(host=host, port=port)
        self.r = redis.Redis(connection_pool=self.pool)
        self.name = queue_name

    def dele(self):
        self.r.delete(self.name)

    def redis_put(self, value):
        return self.r.lpush(self.name, value)

    def redis_get(self):
        return self.r.rpop(self.name)

    def len(self):
        return self.r.llen(self.name)


class SimpleHash(object):
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return (self.cap - 1) & ret


class BloomFilter(object):
    def __init__(self, host='localhost', port=6379, db=0, block_num=1, key='bloom_filter'):
        """
        :param host: the host of Redis
        :param port: the port of Redis
        :param db: witch db in Redis
        :param block_num: one blockNum for about 90,000,000; if you have more strings for filtering, increase it.
        :param key: the key's name in Redis
        """
        self.pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.server = redis.Redis(connection_pool=self.pool)
        self.bit_size = 1 << 31  # Redis的String类型最大容量为512M，现使用256M
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.key = key
        self.blockNum = block_num
        self.hashfunc = []
        for seed in self.seeds:
            self.hashfunc.append(SimpleHash(self.bit_size, seed))

    def is_contains(self, str_input):
        if not str_input:
            return False
        m5 = md5()
        m5.update(str_input.encode('utf8'))
        str_input = m5.hexdigest()
        ret = True
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            ret = ret & self.server.getbit(name, loc)
        return ret

    def insert(self, str_input):
        m5 = md5()
        m5.update(str_input.encode('utf8'))
        str_input = m5.hexdigest()
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            self.server.setbit(name, loc, 1)
