#!/usr/bin/env python
# -- coding: utf-8 --
import time
import re

class Rules(object):
    date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    date_n = re.sub('-', '', date_n)
    date_c = str(int(float(time.time()) * 1000))
    rules_list = [
        # {
        #     'url': [
        #         'http://www.bjda.gov.cn/bjfda/zwgk29/gzdt14/tzgg/tz/index.html'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//ul[@class="list_01"]/li//a/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//h1/text()',
        #         'content': '//td[@class="conzt"]',
        #         'text_f': "臻品艺术网",
        #         'languageVersion': 'ZH',
        #         'category_id': '1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
        # {
        #     'url': [
        #        'http://www.artwer.com/kwzhtml/comprehensive/',
        #         'http://www.artwer.com/kwzhtml/essential/'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//td[@class="heixi14"]/a/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//td[@class="cuhei20"]/text()',
        #         'content': '//td[@class="heixi14ju detailP"]',
        #         'text_f': "尚雅艺术网",
        #         'languageVersion': 'ZH',
        #         'category_id':'1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
        # {
        #     'url': [
        #         'http://www.zhongguolibo.com/libosite/politics/'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//h3/a/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//h1/text()',
        #         'content': '//td[@class="contentddd"]',
        #         'text_f': "中国历博网",
        #         'languageVersion': 'ZH',
        #         'category_id':'1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
        # {
        #     'url': [
        #         'http://new.artsfans.com/news/News!more.htm?sid=3'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//span[@class="news_tit"]/parent::a/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//div[@id="article_tit"]/text()',
        #         'content': '//div[@id="article"]',
        #         'text_f': "中国艺术品收藏网",
        #         'languageVersion': 'ZH',
        #         'category_id':'1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
        # {
        #     'url': [
        #         'http://www.zp798.com/index.php?c=content&a=list&catid=1'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//dl[@class="f_r"]//a/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//h2/text()',
        #         'content': '//div[@class="news_content"]',
        #         'text_f': "臻品艺术网",
        #         'languageVersion': 'ZH',
        #         'category_id':'1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
        # {
        #     'url': [
        #         'http://www.99ys.com/'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//div[@class="title"]//a/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//div[@class="article_title"]/text()',
        #         'content': '//div[@class="article"]',
        #         'text_f': "99艺术网",
        #         'languageVersion': 'ZH',
        #         'category_id':'1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
        # {
        #     'url': [
        #         'http://www.artron.net/newsFlash/'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//ul[@class="txtList30"]/li/a/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//h1/text()',
        #         'content': '//div[@class="detail newsContentDetail"]',
        #         'text_f': "雅昌艺术网",
        #         'languageVersion': 'ZH',
        #         'category_id':'1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
        # {
        #     'url': [
        #         'http://beian.artron.net/newsList.php'
        #     ],
        #     'request_type': 'get',
        #     'datas': {
        #     },
        #     'position': {'url': '//div[@class="newsL"]//li/a[2]/@href'},
        #     'area': '',
        #     'type': 'xpath',
        #     'children_position': {
        #         'title': '//h1/text()',
        #         'content': '//div[@class="detail newsContentDetail"]',
        #         'text_f': "雅昌鉴证备案",
        #         'languageVersion': 'ZH',
        #         'category_id':'1708161040317410000',
        #         'news_date': '//span[@class="time-source"]/text()',
        #     }
        # },
#         {
#             'url': [
#                 'http://www.jingyun68.com/?list-664.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//td[@height="31"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//td[@class="word11BkB"]//b/text()',
#                 'content': '//div[@id="MyContent"]',
#                 'text_f': "北京中古轩艺术品鉴定有限公司",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://news.zhuokearts.com/news.aspx?class_id=1'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//li[@class="l"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="title"]/text()',
#                 'content': '//div[@class="neirong"]',
#                 'text_f': "卓克艺术网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.zgshtzw.com/portal.php?mod=list&catid=41'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h2/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//td[@id="article_content"]',
#                 'text_f': "中国艺术家网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.baozang.com/news/f1028-0'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="nr_ul"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="nrCont"]',
#                 'text_f': "宝藏网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://shoucang.163.com/special/collections_focus/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//span[@class="til"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1[@id="h1title"]/text()',
#                 'content': '//div[@id="endText"]',
#                 'text_f': "网易收藏",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.okcang.cn/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="j-fl"]//a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="wznr-class"]',
#                 'text_f': "汉今收藏网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://news.socang.com/gndt_1.shtml'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//li[@class="if_font2"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="if_wh738 if_font16"]/text()',
#                 'content': '//div[@class="if_wh738_2 if_font18"]',
#                 'text_f': "中国收藏网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://collection.sina.com.cn/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="news-item  "]/h2/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="content"]',
#                 'text_f': "新浪收藏",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://news.cang.com/info/list-2.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="newslist"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//dd[@id="main_content"]',
#                 'text_f': "华夏收藏网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.zgsc2001.com/news/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//a[@class="nszdweizhi"]/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//span[@id="Label3"]/text()',
#                 'content': '//td[@class="neiwen-title"]',
#                 'text_f': "中国收藏新闻网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://guwan.96hq.com/sfgh/',
#                 'http://artist.96hq.com/yxys/',
#                 'http://artist.96hq.com/yhds/',
#                 'http://guwan.96hq.com/gbqb/',
#                 'http://guwan.96hq.com/tqfx/',
#
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//span[@class="lbzdq"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "环球收藏网新闻频道",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.e1988.com/news/list.asp?categoryCID=2%2C7'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//p/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@id="fo"]',
#                 'text_f': "中邮网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.zggjysw.com/NartCover.aspx'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="hangqing_ul"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//span[@id="lblTitle"]/text()',
#                 'content': '//div[@id="pcontent"]',
#                 'text_f': "中国国家艺术网",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.zcxn.com/gdzx.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="scroll"]//a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h3//text()',
#                 'content': '//div[@class="main02-21"]',
#                 'text_f': "中国收藏家协会",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.sssc.cn/b/news/investment/archive/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="scrollnews"]//a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="text_cont_l_tit pr"]/text()',
#                 'content': '//div[@class="text_cont_l_wenmain"]',
#                 'text_f': "盛世收藏",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.caanet.org.cn/News/yejienews.aspx'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="news_lines"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h4/text()',
#                 'content': '//div[@class="con"]',
#                 'text_f': "中国美术家协会",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.chnmuseum.cn/tabid/64/MoreModuleID/517/MoreTabID/40/Default.aspx'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//td[@height="24"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="xl04_tit"]/text()',
#                 'content': '//div[@class="xl04_contm"]/div[@class="xl04_main"]',
#                 'text_f': "国家博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.sach.gov.cn/col/col8/index.html',
#                 'http://www.sach.gov.cn/col/col722/index.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//a[@class="wenwulm"]/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//td[@height="74"]/text()',
#                 'content': '//div[@id="zoom"]',
#                 'text_f': "国家文物局",
#                 'languageVersion': 'ZH',
#                 'category_id':'1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://auction.artron.net/morenews/list16'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="txtList30"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1[@class="title"]/text()',
#                 'content': '//div[@class="detail newsContentDetail"]',
#                 'text_f': "雅昌拍卖",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.cguardian.com/zxzx/jdgg/index.shtml'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="ll"]/div/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="d_title"]/div/text()',
#                 'content': '//div[@class="d_text"]',
#                 'text_f': "中国嘉德国际拍卖有限公司",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.rongbaozhai.cn/index.php?m=content&c=index&a=lists&catid=13'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="title mb5"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="main"]',
#                 'text_f': "荣宝斋",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.sdmuseum.com/channels/ch00009/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//td[@class="lblist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="zx-dis_content"]',
#                 'text_f': "山东博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.tjbwg.com/NewList_10404.html',
#                 'http://www.tjbwg.com/NewList_10405.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="listpictext"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="txttextpage1p"]/text()',
#                 'content': '//div[@class="contentcl"]',
#                 'text_f': "天津博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.hljmuseum.com/zxzx/lbkx/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="titlist04  f14"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h2/text()',
#                 'content': '//div[@class="duanluo"]',
#                 'text_f': "黑龙江省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.hljmuseum.com/zxzx/cpzj/',
#                 'http://www.hljmuseum.com/zxzx/wbzl/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="titlist04  f14"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h2/text()',
#                 'content': '//div[@class="duanluo"]',
#                 'text_f': "黑龙江省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.lnmuseum.com.cn/helt/?ChannelID=460',
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="itemUl112"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//strong/text()',
#                 'content': '//td[@class="articlecont"]',
#                 'text_f': "辽宁省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.lnmuseum.com.cn/helt/?ChannelID=461'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="itemUl112"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h2//text()',
#                 'content': '//td[@class="articlecont"]',
#                 'text_f': "辽宁省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.hebeimuseum.org/channels/95.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h4/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h4/text()',
#                 'content': '//div[@class="mainCont"]/div[@class="bd"]',
#                 'text_f': "河北博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.chnmus.net/wbzs/node_119.htm',
#                 'http://www.chnmus.net/wbzs/node_118.htm'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//td[@class="tu_dian"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//td[@class="zi_16c"]/text()',
#                 'content': '//td[@id="Zoom"]',
#                 'text_f': "河南博物院",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.jxmuseum.cn/bgyw.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//span[@class="STYLE3"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//td[@height="29"]/div//text()',
#                 'content': '//td[@class="main-bg"]/table/tr[2]',
#                 'text_f': "江西省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.hnmuseum.com/zh-hans/xiangbo_dongtai_news',
#                 'http://www.hnmuseum.com/zh-hans/news_guanyi_zixun'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//span[@class="field-content"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="field-items"]/div[@property="content:encoded"]',
#                 'text_f': "湖南省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.gzmuseum.com/zx/gbdt/',
#                 'http://www.gzmuseum.com/zx/zxxx/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h2/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/a/text()',
#                 'content': '//div[@id="Zoom"]',
#                 'text_f': "贵州省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.gdmuseum.com/gdmuseum/_300670/_300702/index.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="txt_cont"]//a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="title"]/text()',
#                 'content': '//div[@class="detail_cont"]',
#                 'text_f': "广东省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.qhmuseum.cn/list-news.html',
#                 'http://www.qhmuseum.cn/list-wenboyaowen.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//dt[@class="fn-frank"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h2[@class="fn-tac"]/text()',
#                 'content': '//div[@id="content"]',
#                 'text_f': "青海省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.ahm.cn/news_5.jsp',
#                 'http://www.ahm.cn/news_3.jsp'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="n_xwdt_list"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h3[@class="h3_txt_info"]/text()',
#                 'content': '//div[@class="txt_info"]',
#                 'text_f': "安徽博物院",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.hainanmuseum.org/xwdt/?tag_id=1'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="new-body"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="title"]/text()',
#                 'content': '//div[@class="article_cont"]',
#                 'text_f': "海南省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#
#         {
#             'url': [
#                 'http://api.bjartmuseum.com/interface/museum/bjww'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//li[@class="scroll-ol"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="newstitle"]/text()',
#                 'content': '//div[@id="zoom"]',
#                 'text_f': "北京艺术博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.jlmuseum.org/news/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="list-txt"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1[@class="article-title"]/text()',
#                 'content': '//div[@class="cont"]',
#                 'text_f': "吉林省博物院",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.shanximuseum.com/about/news/index.html',
#                 'http://www.shanximuseum.com/about/news/wenbo.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="cbox articleList"]//dt/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="pagetitle"]/text()',
#                 'content': '//div[@class="cContainer"]',
#                 'text_f': "山西博物院",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#
#         {
#             'url': [
#                 'https://www.zhejiangmuseum.com/zjbwg/news/zpmnews.html?type=zbkx',
#                 'https://www.zhejiangmuseum.com/zjbwg/news/zpmnews.html?type=sjhd',
#                 'https://www.zhejiangmuseum.com/zjbwg/news/zpmnews.html?type=zlzx'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="newslist topbder m_t_20 p_t_20"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h4/text()[1]',
#                 'content': '//div[@class="zongjie"]',
#                 'text_f': "浙江省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#
#         {
#             'url': [
#                 'http://www.gansumuseum.com/vm_bwg/list_wzxx.aspx?_lmid1=a28263f4-ad42-4ae9-9d27-8ee92e025e04&_lmbh1=008&_lmmc1=%d0%c2%ce%c5&_lmid2=32727ec9-4f62-4d20-bc43-0715aac04f77&_lmbh2=008002&_lmmc2=%ce%c4%b2%a9%b6%af%cc%ac&_lmid3=&_lmbh3=&_lmmc3=&_=c6d622791c994eefb29a5eafb7a9cca4'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="txt_list border"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//span[@id="Label_wzbt"]/text()',
#                 'content': '//div[@class="article_content"]',
#                 'text_f': "甘肃省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.sxhm.com/index.php?ac=article&at=list&tid=223',
#                 'http://www.sxhm.com/index.php?ac=article&at=list&tid=222'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="newslist2"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="bt"]/text()',
#                 'content': '//div[@class="p"]',
#                 'text_f': "陕西历史博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.macaumuseum.gov.mo/w3MMnews/NewsC.aspx?TodayNewsId=88'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h2/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h2/text()[1]',
#                 'content': '//table[@id="ctl00_ContentPlaceHolder1_DetailsView1"]//td[2]',
#                 'text_f': "澳门博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.gxmuseum.cn/a/news/7/index.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="d1 mt2"]//a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h2/text()',
#                 'content': '//td[@id="contentText"]',
#                 'text_f': "广西壮族自治区博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.njmuseum.com/html/News_List@ClassID@194f1ecb-000b-4580-a600-dd57010c8164.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//li[@class="li_title"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//li[@class="list_title"]/text()',
#                 'content': '//li[@class="list_all"]',
#                 'text_f': "南京博物院",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.szmuseum.com/News/Index/Dynamic'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h3/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1[@id="htitle"]/text()',
#                 'content': '//div[@id="divContent"]',
#                 'text_f': "苏州博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.bjww.gov.cn/channel/zlzs/index.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="newsi"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="newstitle"]/text()',
#                 'content': '//div[@id="zoom"]',
#                 'text_f': "北京市文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://wgj.sh.gov.cn/node2/n2029/n2030/n2151/index.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="publist2"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@id="ivs_title"]//text()',
#                 'content': '//div[@id="ivs_content"]',
#                 'text_f': "上海市文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.cqww.gov.cn/channels/41.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="newslist"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="content_content"]',
#                 'text_f': "重庆市文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.haww.gov.cn/wbzx/node_2792.htm'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="r_1"]/ul[1]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1[@id="wzbt"]/text()',
#                 'content': '//div[@id="Zoom"]',
#                 'text_f': "河南文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.sxcr.gov.cn/index.php?m=content&c=index&a=lists&catid=10'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//dl[@class="cl"]/dt/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="content"]',
#                 'text_f': "山西省文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.sdww.gov.cn/xwzx/52.html',
#                 'http://www.sdww.gov.cn/xwzx/55.html',
#                 'http://www.sdww.gov.cn/xwzx/53.html',
#                 'http://www.sdww.gov.cn/xwzx/54.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="txt-list"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="entry"]',
#                 'text_f': "山东文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwu.gov.cn/news?classCode=zfyw',
#                 'http://www.wenwu.gov.cn/news?classCode=wbyw',
#                 'http://www.wenwu.gov.cn/news?classCode=jcdt'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="rightsum1"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h6/text()',
#                 'content': '//div[@id="content"]',
#                 'text_f': "陕西省文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.zjww.gov.cn/zjwb/list.jsp?kind=13'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//td[@width="80%"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//font[@class="unittitle"]/text()',
#                 'content': '//td[@class="content"]',
#                 'text_f': "浙江省文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.gsww.gov.cn/Web_List.aspx?ClsID=26'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="newslist"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="content"]',
#                 'text_f': "甘肃省文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://jsswwj.jiangsu.gov.cn/col/col12967/index.html',
#                 'http://jsswwj.jiangsu.gov.cn/col/col12794/index.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//p/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//title/text()',
#                 'content': '//div[@id="zoom"]',
#                 'text_f': "江苏文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.hbww.gov.cn/staticPath/site001_html/%E6%96%B0%E9%97%BB%E4%B8%AD%E5%BF%83/1.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="content_right_a lf"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="title_1"]/text()',
#                 'content': '//div[@class="detail_content"]',
#                 'text_f': "河北省文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.xjww.com.cn/news/34.aspx'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="newshow_tit"]/text()',
#                 'content': '//div[@class="newshow_content"]',
#                 'text_f': "新疆维吾尔自治区文物局",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
# {
#             'url': [
#                 'http://www.whyn.gov.cn/list/index/1',
#                 'http://www.whyn.gov.cn/list/index/4'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="play_con"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="title"]/text()',
#                 'content': '//div[@class="con"]',
#                 'text_f': "云南省文化厅",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.sckg.com/information',
#                 'http://www.sckg.com/archaeology/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="inner-news-list"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h2[@class="entry-hd"]/text()',
#                 'content': '//div[@class="entry-bd"]',
#                 'text_f': "四川省文物考古研究院",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://hnbwg.hinews.cn/dong_txx.php'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="width692 font_left font_14 lin26"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="width692 font_left font_14 lin26"]',
#                 'text_f': "海南省博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.lnwwkg.com/news_list.asp?type1=1&type2=11'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//table[@width="655"]//td[2]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="STYLE7"]/text()',
#                 'content': '//td[@width="604"]',
#                 'text_f': "辽宁省文物考古研究所",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://museum.fjsen.com/node_167189.htm',
#                 'http://museum.fjsen.com/node_167190.htm'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="list_page"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//td[@id="new_message_id"]',
#                 'text_f': "福建博物院",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.nxbwg.com/cn/02wbdt_2j.asp?SmallClassID=31',
#                 'http://www.nxbwg.com/cn/02wbdt_2j.asp?SmallClassID=7',
#                 'http://www.nxbwg.com/cn/02wbdt_2j.asp?SmallClassID=8'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//td[@width="91%"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//b/text()',
#                 'content': '//div[@class="content"]',
#                 'text_f': "宁夏博物馆",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '16',
#             },
#             'position': {'url': '//div[@class="articlelist_left"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '17',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '18',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '43',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '45',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '46',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '49',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '243',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '244',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '245',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '246',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '247',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '248',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '249',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '250',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '251',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '252',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '253',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '254',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '255',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '256',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '257',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '258',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '259',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '260',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '261',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '262',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '263',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '264',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '265',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '266',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '66',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '46',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '49',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '80',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '82',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '83',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '85',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '217',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '234',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '236',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '232',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '70',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '225',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.wenwuchina.com/article/MmArticle/getList.do'
#             ],
#             'request_type': 'post',
#             'datas': {
#                 'pageNumber': '1',
#                 'pageSize': '40',
#                 'ac_id': '84',
#             },
#             'position': {'url': '//div[@class="newslist"]/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//p[@class="part"]/text()',
#                 'content': '//div[@class="articleDetails_leftA_01"]',
#                 'text_f': "中国文物网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.artsbj.com/list-76-1.html',
#                 'http://www.artsbj.com/list-77-1.html',
#                 'http://www.artsbj.com/list-181-1.html',
#                 'http://www.artsbj.com/list-201-1.html'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="dotUl"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="contentBox"]',
#                 'text_f': "北京文艺网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://art.people.com.cn/GB/226026/index.html',
#                 'http://art.people.com.cn/GB/206244/356129/index.html',
#                 'http://art.people.com.cn/GB/206244/356132/index.html',
#                 'http://art.people.com.cn/GB/206254/206256/index.html',
#                 'http://art.people.com.cn/GB/206254/206255/index.html',
#                 'http://art.people.com.cn/GB/206244/356130/index.html',
#                 'http://art.people.com.cn/GB/206246/408046/index.html',
#                 'http://art.people.com.cn/GB/206246/408047/index.html',
#                 'http://art.people.com.cn/GB/206261/index.html',
#
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h4/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="box_con"]',
#                 'text_f': "人民网-书画",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://shuhua.gmw.cn/node_10673.htm',
#                 'http://shuhua.gmw.cn/node_11584.htm',
#                 'http://shuhua.gmw.cn/node_9004.htm',
#                 'http://shuhua.gmw.cn/node_11593.htm',
#                 'http://shuhua.gmw.cn/node_11586.htm',
#                 'http://shuhua.gmw.cn/node_9011.htm',
#                 'http://shuhua.gmw.cn/node_11592.htm',
#                 'http://shuhua.gmw.cn/node_11585.htm',
#                 'http://shuhua.gmw.cn/node_9661.htm',
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="channel-newsGroup"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@id="contentMain"]',
#                 'text_f': "光明网书画频道",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://news.cang.com/info/list-1.html',
#                 'http://news.cang.com/info/list-2.html',
#                 'http://news.cang.com/info/list-22.html',
#                 'http://news.cang.com/info/list-7.html',
#                 'http://news.cang.com/info/list-10.html',
#                 'http://news.cang.com/info/list-9.html',
#                 'http://news.cang.com/info/list-23.html',
#                 'http://news.cang.com/info/list-3.html',
#                 'http://news.cang.com/info/list-8.html',
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="newslist"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//dd[@id="main_content"]',
#                 'text_f': "华夏收藏网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.cnarts.net/cweb/news/news_list.asp?kind=%D2%D5%CA%F5',
#                 'http://www.cnarts.net/cweb/news/news_list.asp?kind=%D5%B9%C0%C0',
#                 'http://www.cnarts.net/cweb/news/news_list.asp?kind=%BC%AF%B2%D8',
#                 'http://www.cnarts.net/cweb/news/news_list.asp?kind=%C5%C4%C2%F4',
#                 'http://www.cnarts.net/cweb/Process/index_read.asp?kind=%B9%A4%D2%D5%D0%C5%CF%A2',
#                 'http://www.cnarts.net/cweb/Appreciation_collection/index_read.asp?kind=%CA%D5%B2%D8%CE%C4%D5%AA#',
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="list_in_er"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//div[@class="read_news_content_title"]/h2/text()',
#                 'content': '//div[@class="read_news_content1"]',
#                 'text_f': "中国艺术品新闻中心",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.ccdy.cn/wenwu/',
#                 'http://www.ccdy.cn/yishu/'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h3/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="TRS_Editor"]',
#                 'text_f': "中国文化传媒网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://art.china.cn/zixun/node_517362.htm'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@class="main"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="content"]',
#                 'text_f': "艺术中国",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://roll.collection.sina.com.cn/collection/yjjj/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/zgsh/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/qbtd/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/ddys/yh32/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/ddys/ds14/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/ddys/sm15/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/ddys/bh7/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/yhds/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/cqty/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/wwzx/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/gjsb/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/tqfx/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/qbtd/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/zwyp/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/fcys/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/jjhm/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/scsx1/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/qtcp/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/hwdt/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/pmzx/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/pmzx/pcdt/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/zlxx/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/cpsc/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/jczs2/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/cqyw/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/cjrw1/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/plfx/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/zspd1/yjzx1/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/gjsb/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/wwzx/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/yhds/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/tqfx/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/qbtd/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/zwyp/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection/cqty/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/jjhm/yjzx1/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/jjhm/hmsc/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/jjhm/hmrw/index.shtml',
#                 'http://roll.collection.sina.com.cn/collection_1/jjhm/hmbk/index.shtml',
#                 'http://roll.collection.sina.com.cn/s/channel.php?ch=16#col=153&spec=&type=&ch=16&k=&offset_page=0&offset_num=0&num=60&asc=&page=1',
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="list"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="content"]',
#                 'text_f': "新浪收藏",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://interface.sina.cn/collection/pc_whcy_yjtt_list_index.d.html?cid=whzx',
#                 'http://interface.sina.cn/collection/pc_yszb_hyxw_list_index.html',
#                 'http://interface.sina.cn/collection/pc_shpd_yjzx_list_index.d.html',
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="list"]/li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="content"]',
#                 'text_f': "新浪收藏",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://culture.china.com/art/',
#
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//ul[@class="newslist"]//a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@id="chan_newsDetail"]',
#                 'text_f': "中华网文化频道",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://www.gscn.com.cn/culture/sckg/index.shtml',
#                 'http://shuhua.gscn.com.cn/shzx/',
#                 'http://shuhua.gscn.com.cn/gwsc/',
#                 'http://shuhua.gscn.com.cn/mszt/',
#                 'http://shuhua.gscn.com.cn/ghmj/',
#                 'http://shuhua.gscn.com.cn/shjs/',
#                 'http://shuhua.gscn.com.cn/shyj/',
#                 'http://shuhua.gscn.com.cn/pmdt/',
#                 'http://shuhua.gscn.com.cn/shjx/',
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//div[@id="content"]//li/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@class="a-container"]',
#                 'text_f': "中国甘肃网",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },
#         {
#             'url': [
#                 'http://hn.ifeng.com/listpage/2859/1/list.shtml'
#             ],
#             'request_type': 'get',
#             'datas': {
#             },
#             'position': {'url': '//h2/a/@href'},
#             'area': '',
#             'type': 'xpath',
#             'children_position': {
#                 'title': '//h1/text()',
#                 'content': '//div[@id="main_content"]',
#                 'text_f': "凤凰网河南",
#                 'languageVersion': 'ZH',
#                 'category_id': '1708161040317410000',
#                 'news_date': '//span[@class="time-source"]/text()',
#             }
#         },

    ]


if __name__ == '__main__':
    pass
