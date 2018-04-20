#!/usr/bin/env python
# -- coding: utf-8 --

if __name__ == '__main__':
    import json
    a = {'a': 1, 'b': None, 'c': False}
    b = json.dumps(a)
    print(b)
    c = json.loads(b)
    print(c)
