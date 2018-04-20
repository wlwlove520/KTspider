## KTspider

### 基于Python3的异步爬虫框架
#### Python3.6以上版本

1. 页面匹配规则具有可插拔性
2. 暂时可以使用xpath，re模块来进行页面匹配
3. 可以满足不同的定制化需求
4. 设计符合自己的存储方式

### 启动
```
python run.py
```

### 使用
rules.py 文件是所有规则整理的地方，可以把所有的规则写入到rules.py文件
参考如下规则：
```
rules_list = [
        {
            'url': ['http://cq.cqnews.net/szjz/index.htm'],
            'position': {'url': '//div[@class="lb"]/ul/li/a/@href'},
            'area': '重庆市',
            'type': 'xpath',
            'children_position': {
                'title': '//h1/text()',
                'content': '//*[@id="_h5_content"]',
                'news_date': '//*[@id="smalltitle"]/span[2]/text()',
                'text_f': '华龙网'
            }
        },
        {
            'url': ['http://cq.qq.com/CQxinwen/chongqi/cqnews.htm'],
            'position': {'url': '//*[@id="page_1"]/li/span/a/@href'},
            'area': '重庆市',
            'type': 'xpath',
            'children_position': {
                'title': '//h1/text()',
                'content': '//*[@id="Cnt-Main-Article-QQ"]',
                'news_date': '//div/span[contains(@class, "article-time")]/text()',
                'text_f': '大渝新闻'
            }
        }]
```

作为一个开放性很高的爬虫框架，当然允许进行一些个性操作了。
比如说总会有一些需求不能在rules.py文件里完美实现。

那么请参考如下script.py文件的代码注释：
```
class Task(object):
    def __init__(self, rules):
        self.task = self.get_task()
        self.rules = rules

    def get_task(self):
        for rule in self.rules:
            try:
                for u in rule.get('url'):
                    yield {'url': [u], 'retry': 0}
            except:
                continue

    async def process_result(self, task, result):
        """
        page parser
        页面跳转定制化函数，接收请求页面源码和task
        返回子页面的task或者子页面的解析结果
        """
        task['url'] = [task.get('url')]
        task = self.get_gen(task)
        return result, None

    def get_gen(self, task):
        return (i for i in [task])
```

save_result.py文件是为存储设计的，当然只写了mysql存储，其余存储操作可操作save()函数：
```
    async def save(self, url, result) -> bool:
        """
        save result
        :param url:
        :param result:
        :return: true or false
        """
        logging.debug("%s start: url=%s", self.__class__.__name__, url)

        try:
            self._save_pip.write(json.dumps(result_out))
            self._save_pip.flush()
            save_result = True
        except IndexError as e:
            save_result = False
            res = json.loads(result)
            logging.error("%s error: %s， area: %s, source: %s", self.__class__.__name__, e, res.get('area'), res.get('text_f'))
        except Exception as e:
            save_result = False
            logging.error("%s error: %s, url=%s", self.__class__.__name__, e, url)

        logging.debug("%s end: save_result=%s, url=%s", self.__class__.__name__, save_result, url)
        return save_result
```
### TODO
- 增加控制台
- 优化图片下载
- 进一步封装各部分
