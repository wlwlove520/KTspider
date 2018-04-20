#!/usr/bin/env python
# -- coding: utf-8 --
from KTqueue import bloom_filter

q = bloom_filter.Queue('OBS_IMG_QUEUE')
print(q.len())

if __name__ == '__main__':
    pass