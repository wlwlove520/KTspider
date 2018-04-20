#!/usr/bin/env python
# -- coding: utf-8 --
import sys, os
import json
import logging
import re
import collections
from urllib.parse import urljoin

from lxml import etree

from tools.filter_file import extract_url,filter_url

sys.path.append(os.getcwd())


class Task(object):
    def __init__(self, rules):
        self.task = self.get_task()
        self.rules = rules

    def get_task(self):
        for rule in self.rules:
            try:
                yield {'url': rule.get('url'),
                       'request_type': rule.get('request_type'),
                       'datas': rule.get('datas'),
                       'position': rule.get('position'),
                       'area': rule.get('area'),
                       'type': rule.get('type'),
                       'children_position': rule.get('children_position'),
                       'is_children': False,
                       'retry': 0,
                       }
            except:
                continue


    async def process_result(self, task, result):
        """
        page parser
        页面跳转定制化函数，接收请求页面源码和task
        返回子页面的task或者子页面的解析结果
        """
        r = collections.defaultdict()
        parse_type = task.get('type')
        is_children = task.get('is_children')
        position = task.get('position')
        url = task.get('url')
        us = []
        try:
            if parse_type == 'xpath':
                # print(result)
                us = extract_url(url,result)

                doc = etree.HTML(result)
                for key in position.keys():
                    xpath_rule = position.get(key)
                    if not xpath_rule:
                        r[key] = ['', '']
                        continue
                    if key == 'text_f' or key == 'languageVersion' or key == 'category_id':
                        r[key] = xpath_rule
                        continue

                    if key == 'content':
                        r[key] = etree.tostring(doc.xpath(xpath_rule)[0], xml_declaration=True,
                                                encoding='utf-8').decode()
                        continue

                    r[key] = doc.xpath(xpath_rule)
            elif parse_type == 're':
                for key in position.keys():
                    r[key] = re.findall(position.get(key), result)
        except IndexError as e:
            logging.error('IndexError: %s', e)
        except Exception as e:
            logging.error('parse error: %s', e)

        if is_children:
            r['area'] = task.get('area')
            r['obj_url'] = task.get('obj_url')
            return json.dumps(r), None

        task['is_children'] = True
        task['position'] = task.get('children_position')
        task['request_type'] = 'get'

        if len(us):
            task["url"] = us
        else:
            try:
                task['url'] = [urljoin(url, u) for u in r.get('url')[:3]]
            except:
                pass
        task['url'] = filter_url(url,task['url'])
        task['obj_url'] = url
        task = self.get_gen(task)
        return None, task

    def get_gen(self, task):
        return (i for i in [task])


if __name__ == '__main__':
    pass
