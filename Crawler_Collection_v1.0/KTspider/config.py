#!/usr/bin/env python
# -- coding: utf-8 --
import random
import time
import os

'''
项目名称
'''
OBJECT_NAME = "KTspider"

'''
watcher path
'''
WATCHER_PATH = "watcher.info"

'''
开发者
'''
BY = "WULEWEI"
FUN_BIG_DATA = "SC-news"  # 值为模块拼音首字母大写
FUN_AND_NUM = {
    'XW-news':          '001',                   # 本地新闻和分类新闻
    'XW-index':         '002',                   # 新闻 推荐
    'WZ-laws':          '101',                   # 问政法律
    'WZ-news':          '102',                   # 问政资讯
    'WZ-mayor':         '103',                   # 问政领导人
    'SJ-opportunity':   '201',                   # 商机项目
    'SJ-tank':          '202',                   # 商机机构
    'SJ-all':           '203',                   # 商机资讯
    'SD-channel':       '301',                   # 商道资讯
    'YD-entertainment': '401',                   # 娱道资讯
    'SC-news':          '501',                   # 收藏资讯
    'SC-products':      '502',                   # 收藏馆藏和作品
    'GY-all':           '601',                   # 公益资讯
    'LY-tour':          '701',                   # 旅游资讯
    'YP-news':          '801',                   # 优品资讯
    'ZS-news':          '901'                    # 掌视资讯
}
DEVELOPER = {
    'WULEWEI': '0001',
}
'''
logger name
'''
# logger_data = '/home/admin/spider2flume/data/'+str(int(time.time()))
# logger_log = '/home/admin/spider2flume/logs/'+str(int(time.time()))
DATA_FILE_NAME = './cp_data/data/'+str(int(time.time()))+BY+'.txt'
LOG_FILE_NAME_RUN = './log/run_log/'+str(int(time.time()))+BY+'.txt'
LOGS_FILE_NAME = './cp_data/logs/'+str(int(time.time()))+BY+'.txt'

'''
mysql setting
'''
HOST_MYSQL = "127.0.0.1"
PORT_MYSQL = "3306"
DATABASE_MYSQL = "spider"
USER_MYSQL = ""
PASSWORD_MYSQL = ""
CHARSET_MYSQL = "utf8"

'''
redis setting
'''
HOST = '127.0.0.1'
PORT = '6379'



'''
kafka setting
'''
DATA_TOPIC = "spider"
LOG_TOPIC = "spider_log"
BOOTSTRAP_SERVERS = ["192.168.5.240:9092"]
# BOOTSTRAP_SERVERS = ["192.168.1.254:19092","192.168.1.172:19092","192.168.1.97:19092"]


'''
OSS config
'''
ACCESS_KEY_ID = ""
ACCESS_KEY_SECRET = ""
OSS_HOST = ""
OSS_BUCKET = ""
OSS_BUCKET_HOST = ""

"""
obs config
"""
AK = ''
SK = ''
SERVER = ''
REGION = ''
SIGNATURE = ''
BUCKET_NAME = ''

"""
消息队列名
"""
QUEUE_IMG_NAME = "OBS_IMG_QUEUE"
QUEUE_IMG_NAME_WARN = "OBS_IMG_WARN_QUEUE"
QUEUE_IMG_NAME_ERROR = "OBS_IMG_ERROR_QUEUE"
QUEUE_DATA_NAME = "SQ_put_data"

"""
消息头
"""
CITY_PARLOR_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'cookie': '_user_id=1708281259017703024; _user_account=suqi;',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

"""
后台上传地址
"""
CITY_PARLOR_NEWS_SAVE_URL = "http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save"
CITY_PARLOR_REC_NEWS_SAVE_URL = "http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/index/add"
OBS_IMG_PATH = "https://sq.obs.myhwclouds.com/img/{date}"

'''
USER_AGENTS 随机头信息
'''
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

'''
城市及编码
'''
AREA_DICT = {
'欧洲':'EUR',
'非洲':'AFR',
'北美洲':'NOR',
'大洋洲':'OCE',
'南美洲':'SOU',
'日本':'001',
'东京':'00101',
'横滨':'00102',
'大阪':'00103',
'名古屋':'00104',
'札幌':'00105',
'神户':'00106',
'京都':'00107',
'韩国':'002',
'首尔':'00201',
'釜山':'00203',
'仁川':'00205',
'济州':'00217',
'朝鲜':'003',
'平壤':'00301',
'蒙古':'004',
'乌兰巴托':'00401',
'达尔汗乌勒省':'00421',
'戈壁苏木贝尔省':'00422',
'菲律宾':'005',
'马尼拉':'00504',
'柬埔寨':'006',
'金边':'00613',
'老挝':'007',
'万象':'00701',
'马来西亚':'008',
'马六甲':'00804',
'吉隆坡':'00814',
'缅甸':'009',
'仰光':'00907',
'内比都':'00915',
'泰国':'010',
'曼谷':'01001',
'清迈':'01038',
'普吉':'01061',
'文莱':'011',
'越南':'012',
'河内':'01216',
'胡志明':'01217',
'东帝汶':'013',
'帝力':'01304',
'新加坡共和国':'014',
'印度尼西亚':'015',
'雅加达':'01501',
'万隆':'01504',
'巴基斯坦':'016',
'伊斯兰堡':'01602',
'不丹':'017',
'廷布':'01701',
'马尔代夫':'018',
'马累':'01801',
'孟加拉国':'019',
'达卡':'01901',
'尼泊尔':'020',
'斯里兰卡':'021',
'科伦坡':'02101',
'印度':'022',
'新德里':'02226',
'哈萨克斯坦':'023',
'阿斯塔纳':'02301',
'吉尔吉斯斯坦':'024',
'比什凯克':'02407',
'塔吉克斯坦':'025',
'杜尚别':'02501',
'乌兹别克斯坦':'026',
'塔什干':'02613',
'土库曼斯坦':'027',
'阿什哈巴德':'02701',
'阿富汗':'028',
'喀布尔':'02801',
'黎巴嫩':'029',
'贝鲁特':'02901',
'叙利亚':'030',
'大马士革':'03001',
'伊拉克':'031',
'巴格达':'03101',
'伊朗':'032',
'德黑兰':'03201',
'约旦':'033',
'安曼':'03302',
'阿拉伯联合酋长国':'034',
'阿布扎比':'03401',
'迪拜':'03402',
'沙迦':'03403',
'巴林':'035',
'麦纳麦':'03501',
'卡塔尔':'036',
'多哈':'03601',
'科威特':'037',
'科威特':'03702',
'沙特阿拉伯':'038',
'利雅得':'03801',
'麦加':'03803',
'以色列':'039',
'西耶路撒冷':'03901',
'巴勒斯坦':'040',
'东耶路撒冷':'04001',
'阿曼':'041',
'马斯喀特':'04101',
'阿塞拜疆':'042',
'巴库':'04201',
'格鲁吉亚':'043',
'第比利斯':'04301',
'塞浦路斯':'044',
'尼科西亚':'04401',
'土耳其':'045',
'安卡拉':'04504',
'伊斯坦布尔':'04513',
'亚美尼亚':'046',
'埃里温':'04601',
'也门':'047',
'萨那':'047113',
'冰岛':'048',
'雷克雅未克':'04801',
'丹麦':'049',
'哥本哈根':'04901',
'芬兰':'050',
'赫尔辛基':'05001',
'挪威':'051',
'奥斯陆':'05101',
'瑞典':'052',
'斯德哥尔摩':'05201',
'哥德堡':'05202',
'爱沙尼亚':'053',
'塔林':'05301',
'白俄罗斯':'054',
'明斯克':'05401',
'俄罗斯':'055',
'莫斯科':'05501',
'圣彼得堡':'05502',
'叶卡捷琳堡':'05505',
'拉脱维亚':'056',
'里加':'05601',
'立陶宛':'057',
'维尔纽斯':'05701',
'摩尔多瓦':'058',
'基希讷乌':'05801',
'乌克兰':'059',
'基辅':'05901',
'奥地利':'060',
'维也纳':'06001',
'波兰':'061',
'华沙':'06101',
'德国':'062',
'不来梅':'06202',
'杜塞尔多夫':'06204',
'慕尼黑':'06206',
'柏林':'06208',
'汉堡':'06210',
'捷克':'063',
'布拉格':'06301',
'列支敦士登':'064',
'瓦杜兹':'06401',
'瑞士':'065',
'苏黎世':'06501',
'日内瓦':'06502',
'伯尔尼':'06504',
'洛桑':'06505',
'斯洛伐克':'066',
'布拉迪斯拉发':'06601',
'匈牙利':'067',
'布达佩斯':'06701',
'爱尔兰':'068',
'都柏林':'06801',
'比利时':'069',
'布鲁塞尔':'06901',
'法国':'070',
'巴黎':'07001',
'里昂':'07013',
'波尔多':'07015',
'尼斯':'07018',
'马赛':'07020',
'荷兰':'071',
'海牙':'07102',
'卢森堡大公国':'072',
'卢森堡':'07203',
'摩纳哥':'073',
'蒙特卡洛':'07301',
'英国':'074',
'伦敦':'07401',
'曼彻斯特':'07402',
'利物浦':'07403',
'伯明翰':'07404',
'爱丁堡':'07405',
'格拉斯哥':'07406',
'贝尔法斯特':'07407',
'阿尔巴尼亚':'075',
'地拉那':'07501',
'保加利亚':'076',
'索非亚':'07601',
'罗马尼亚':'077',
'布加勒斯特':'07701',
'马其顿':'078',
'斯科普里':'07801',
'塞尔维亚':'079',
'贝尔格莱德':'07901',
'希腊':'080',
'雅典':'08001',
'斯洛文尼亚':'081',
'卢布尔雅那':'08101',
'克罗地亚':'082',
'萨格勒布':'08201',
'波黑':'083',
'萨拉热窝':'08301',
'意大利':'084',
'罗马':'08401',
'米兰':'08402',
'佛罗伦萨':'08403',
'那不勒斯':'08404',
'威尼斯':'08405',
'都灵':'08406',
'梵地冈':'085',
'梵蒂冈城':'08501',
'圣马力诺共和国':'086',
'马尔他':'087',
'瓦莱塔':'08701',
'西班牙':'088',
'马德里':'08801',
'巴塞罗那':'08802',
'葡萄牙':'089',
'里斯本':'08901',
'安道尔':'090',
'安道尔城':'09001',
'埃及':'091',
'开罗':'09101',
'亚历山大':'09102',
'阿斯旺':'09106',
'利比亚':'092',
'的黎波里':'09201',
'班加西':'09202',
'苏丹':'093',
'喀土穆':'09301',
'阿尔及利亚':'094',
'阿尔及尔':'09401',
'摩洛哥':'095',
'拉巴特':'09501',
'突尼斯':'096',
'突尼斯':'09601',
'埃塞俄比亚':'097',
'亚的斯亚贝巴':'09701',
'索马里':'098',
'摩加迪沙':'09801',
'吉布提':'099',
'吉布提':'09901',
'肯尼亚':'100',
'内罗毕':'10001',
'坦桑尼亚':'101',
'多多玛':'10101',
'乌干达':'102',
'坎帕拉':'10201',
'卢旺达':'103',
'基加利':'10301',
'布隆迪':'104',
'布琼布拉':'10401',
'塞舌尔':'105',
'维多利亚':'10501',
'厄立特里亚':'106',
'阿斯马拉':'10601',
'乍得':'107',
'恩贾梅纳':'10701',
'班吉':'10801',
'比劳':'10802',
'布里亚':'10803',
'奥博':'10804',
'赤道几内亚':'109',
'马拉博':'10901',
'巴塔':'10902',
'喀麦隆':'110',
'雅温得':'11001',
'加蓬':'111',
'利伯维尔':'11101',
'刚果金':'112',
'金沙萨':'11201',
'刚果（布）':'113',
'布拉柴维尔':'11301',
'圣多美和普林西比':'114',
'圣多美':'11401',
'毛里塔尼亚':'115',
'努瓦克肖特':'11501',
'塞内加尔':'116',
'达喀尔':'11601',
'冈比亚':'117',
'班珠尔':'11701',
'马里':'118',
'巴马科':'11801',
'布基纳法索':'119',
'瓦加杜古':'11901',
'几内亚':'120',
'科纳克里':'12001',
'几内亚比绍':'121',
'比绍':'12101',
'阿尤恩':'12201',
'达赫拉':'12202',
'斯马拉':'12203',
'佛得角':'123',
'普拉亚':'12301',
'塞拉利昂':'124',
'弗里敦':'12401',
'利比里亚':'125',
'蒙罗维亚':'12501',
'科特迪瓦':'126',
'亚穆苏克罗':'12601',
'多哥':'127',
'洛美':'12701',
'贝宁':'128',
'波多诺伏':'12801',
'加纳':'129',
'阿克拉':'12901',
'尼日尔':'130',
'尼亚美':'13001',
'尼日利亚':'131',
'阿布贾':'13101',
'罗安达':'13201',
'卡宾达':'13202',
'万博':'13203',
'本格拉':'13204',
'赞比亚':'133',
'卢萨卡':'13301',
'津巴布韦':'134',
'哈拉雷':'13401',
'马拉维':'135',
'利隆圭':'13501',
'莫桑比克':'136',
'马普托':'13601',
'博茨瓦纳':'137',
'哈博罗内':'13701',
'纳米比亚':'138',
'温得和克':'13801',
'南非':'139',
'茨瓦内':'13901',
'开普敦':'13902',
'布隆方丹':'13903',
'约翰内斯堡':'13904',
'伊丽莎白港':'13905',
'德班':'13906',
'斯威士兰':'140',
'姆巴巴内':'14001',
'莱索托':'141',
'马塞卢':'14101',
'马达加斯加':'142',
'塔那那利佛':'14201',
'科摩罗':'143',
'莫罗尼':'14301',
'毛里求斯':'144',
'路易港':'14401',
'澳大利亚':'145',
'堪培拉':'14501',
'悉尼':'14502',
'墨尔本':'14503',
'布里斯班':'14505',
'阿德莱德':'14508',
'新西兰':'146',
'惠灵顿':'14601',
'奥克兰':'14602',
'基督城':'14603',
'巴布亚新几内亚':'147',
'莫尔斯比港':'14701',
'所罗门群岛':'148',
'霍尼亚拉':'14801',
'瓦努阿图':'149',
'维拉港':'14901',
'密克罗尼西亚':'150',
'帕利基尔':'15001',
'马绍尔群岛':'151',
'马朱罗':'15101',
'帕劳':'152',
'梅莱凯奥克':'15201',
'瑙鲁':'153',
'亚伦':'15301',
'基里巴斯':'154',
'塔拉瓦':'15401',
'图瓦卢':'155',
'富纳富提':'15501',
'萨摩亚':'156',
'阿皮亚':'15601',
'斐济':'157',
'苏瓦':'15701',
'汤加':'158',
'努库阿洛法':'15801',
'阿瓦鲁阿':'15901',
'努美阿':'16001',
'阿洛菲':'16101',
'美国':'162',
'华盛顿':'16201',
'纽约':'16202',
'洛杉矶':'16203',
'芝加哥':'16204',
'休斯敦':'16205',
'费城':'16206',
'旧金山':'16207',
'波士顿':'16208',
'匹兹堡':'16209',
'加拿大':'163',
'渥太华':'16301',
'多伦多':'16302',
'蒙特利尔':'16303',
'温哥华':'16304',
'卡尔加里':'16305',
'温尼伯':'16307',
'墨西哥':'164',
'墨西哥城':'16401',
'危地马拉':'165',
'危地马拉城':'16501',
'伯利兹':'166',
'贝尔莫潘':'16601',
'萨尔瓦多':'167',
'圣萨尔瓦多':'16701',
'洪都拉斯':'168',
'特古西加尔巴':'16801',
'尼加拉瓜':'169',
'马那瓜':'16901',
'哥斯达黎加':'170',
'圣何塞':'17001',
'巴拿马':'171',
'巴拿马城':'17101',
'巴哈马':'172',
'拿骚':'17201',
'古巴':'173',
'哈瓦那':'17301',
'牙买加':'174',
'金斯敦':'17401',
'海地':'175',
'太子港':'17501',
'多米尼加':'176',
'圣多明各':'17601',
'安提瓜和巴布达':'177',
'圣约翰':'17701',
'圣基茨和尼维斯':'178',
'巴斯特尔':'17801',
'多米尼克':'179',
'罗索':'17901',
'圣文森特和格林纳丁斯':'180',
'金斯敦':'18001',
'格林纳达':'181',
'圣乔治':'18101',
'巴巴多斯':'182',
'布里奇顿':'18201',
'特立尼达和多巴哥':'183',
'西班牙港':'18301',
'圣胡安':'18401',
'马亚圭斯':'18402',
'蓬塞':'18403',
'罗德城':'18501',
'委内瑞拉':'186',
'加拉加斯':'18601',
'圭亚那':'188',
'乔治敦':'18801',
'苏里南':'189',
'帕拉马里博':'18901',
'厄瓜多尔':'190',
'基多':'19001',
'秘鲁':'191',
'利马':'19101',
'玻利维亚':'192',
'苏克雷':'19202',
'巴西':'193',
'巴西利亚':'19301',
'圣保罗':'19302',
'里约热内卢':'19303',
'马瑙斯':'19304',
'伊瓜苏':'19306',
'智利':'194',
'圣地亚哥':'19401',
'阿根廷':'195',
'布宜诺斯艾利斯':'19501',
'巴拉圭':'196',
'亚松森':'19601',
'乌拉圭':'197',
'蒙得维的亚':'19710',
'亚洲':'ASI',
'黄冈':'421100',
'安徽':'340000',
'鄂尔多斯':'150600',
'常州':'320400',
'宿州':'341300',
'湘西':'433100',
'神农架':'429021',
'平顶山':'410400',
'中山':'442000',
'潍坊':'370700',
'昌邑':'370786',
'营口':'210800',
'鹤岗':'230400',
'娄底':'431300',
'金昌':'620300',
'绍兴':'330600',
'驻马店':'411700',
'长治':'140400',
'天门':'429006',
'潜江':'429005',
'仙桃':'429004',
'贵州':'520000',
'湖南':'430000',
'积石山':'622927',
'广河':'622924',
'永靖':'622923',
'东乡':'622926',
'和政':'622925',
'康乐':'622922',
'青州':'370781',
'乐山':'511100',
'襄阳':'420600',
'韶关':'440200',
'临夏':'622901',
'新余':'360500',
'宁夏':'622900',
'大石桥':'210882',
'安康':'610900',
'吉林':'220200',
'汕尾':'441500',
'日喀则':'542300',
'石家庄':'130100',
'黔南':'522700',
'朝阳':'211300',
'贵阳':'520100',
'日照':'371100',
'辽宁':'210000',
'张家界':'430800',
'梧州':'450400',
'嘉峪关':'620200',
'临高县':'469028',
'澄迈':'469027',
'屯昌':'469026',
'定安':'469025',
'迪庆':'533400',
'厦门':'350200',
'南沙群岛':'469038',
'西沙群岛':'469037',
'琼中':'469036',
'保亭':'469035',
'陵水':'469034',
'乐东':'469033',
'昌江':'469031',
'白沙':'469030',
'万宁':'469006',
'文昌':'469005',
'儋州':'469003',
'琼海':'469002',
'五指山':'469001',
'东方':'469007',
'丽水':'331100',
'大理':'532901',
'大理':'532900',
'海北':'632200',
'曲靖':'530300',
'陕西':'610000',
'绵阳':'510700',
'肥西':'340123',
'济宁':'370800',
'合肥':'340100',
'沧州':'130900',
'揭阳':'445200',
'通辽':'150500',
'苏州':'320500',
'阜新':'210900',
'双鸭山':'230500',
'咸宁':'421200',
'安宁':'530181',
'安阳':'410500',
'金华':'330700',
'长沙县':'430121',
'长沙':'430100',
'任丘':'130982',
'神木':'610821',
'府谷':'610822',
'阳泉':'140300',
'霍林郭勒':'150581',
'鹰潭':'360600',
'榆林':'610800',
'内江':'511000',
'百色':'451000',
'牡丹江':'231000',
'德阳':'510600',
'黔东':'522600',
'葫芦岛':'211400',
'山南':'542200',
'鄂州':'420700',
'莱芜':'371200',
'深圳':'440300',
'兰州':'620100',
'沈阳':'210100',
'怒江':'533300',
'莆田':'350300',
'大同':'140200',
'河源':'441600',
'扬州':'321000',
'兴安盟':'152200',
'西双版纳':'532800',
'抚州':'361000',
'益阳':'430900',
'北海':'450500',
'河北':'130000',
'潮州':'445100',
'海东':'632100',
'巴中':'511900',
'临沧':'530900',
'嘉善':'330421',
'白城':'220800',
'酒泉':'620900',
'嘉兴':'330400',
'信阳':'411500',
'巴彦淖尔':'150800',
'永州':'431100',
'开封':'410200',
'东营':'370500',
'宁德':'350900',
'德宏':'533100',
'广东':'440000',
'广饶':'370523',
'丹东':'210600',
'汉中':'610700',
'齐齐哈尔':'230200',
'惠州':'441300',
'淮北':'340600',
'朔州':'140600',
'昆明':'530100',
'岳阳':'430600',
'雅安':'511800',
'柳州':'450200',
'甘肃':'620000',
'泸州':'510500',
'吉林':'220000',
'景德镇':'360200',
'宜兴':'320282',
'盘锦':'211100',
'秦皇岛':'130300',
'昌都':'542100',
'天长':'341181',
'天津':'120100',
'湛江':'440800',
'巩义':'410181',
'荥阳':'410182',
'新郑':'410184',
'福建':'350000',
'临汾':'141000',
'海宁':'330481',
'桐乡':'330483',
'无锡':'320200',
'滁州':'341100',
'海西':'632800',
'福清':'350181',
'阜阳':'341200',
'平凉':'620800',
'荆州':'421000',
'德清':'330521',
'长兴':'330522',
'宜都':'420581',
'洛阳':'410300',
'湖州':'330500',
'烟台':'370600',
'普洱':'530800',
'呼伦贝尔':'150700',
'锦州':'210700',
'延安':'610600',
'鸡西':'230300',
'锡林郭勒':'152500',
'怀化':'431200',
'黔西':'522300',
'周口':'411600',
'西昌':'513401',
'凉山':'513400',
'莱州':'370683',
'招远':'370685',
'宜昌':'420500',
'铜陵':'340700',
'广州':'440100',
'九江':'360400',
'重庆':'500100',
'晋城':'140500',
'双阳':'220112',
'安庆':'340800',
'唐山':'130200',
'长春':'220100',
'南关':'220102',
'朝阳区':'220104',
'宽城':'220103',
'萍乡':'360300',
'梅州':'441400',
'陇南':'621200',
'达州':'511700',
'毕节':'522400',
'攀枝花':'510400',
'铁岭':'211200',
'新沂':'320381',
'云南':'530000',
'上海':'310100',
'榆树':'220182',
'九台':'220181',
'德惠':'220183',
'威海':'371000',
'常德':'430700',
'渭南':'610500',
'桂林':'450300',
'玉环':'331021',
'甘南':'623000',
'福州':'350100',
'台州':'331000',
'商洛':'611000',
'文山':'532600',
'沛县':'320322',
'茂名':'440900',
'徐州':'320300',
'宁波':'330200',
'南阳':'411300',
'运城':'140800',
'玉树':'632700',
'资阳':'512000',
'玉林':'450900',
'河南':'410000',
'黄石':'420200',
'丽江':'530700',
'宜春':'360900',
'白山':'220600',
'西宁':'630100',
'铜仁':'522200',
'淮南':'340400',
'保定':'130600',
'包头':'150200',
'淮安':'320800',
'滨州':'371600',
'济源':'410881',
'池州':'341700',
'焦作':'410800',
'淄博':'370300',
'南平':'350700',
'衡阳':'430400',
'樟树':'360982',
'广西':'450000',
'甘孜':'513300',
'恩施':'422800',
'抚顺':'210400',
'黑龙江':'230000',
'张掖':'620700',
'来宾':'451300',
'定西':'621100',
'红河':'532500',
'佛山':'440600',
'托克托':'150122',
'广安':'511600',
'莱西':'370285',
'三亚':'460200',
'咸阳':'610400',
'自贡':'510300',
'江西':'360000',
'江苏':'320000',
'廊坊':'131000',
'东莞':'441900',
'青海':'630000',
'香河':'131024',
'宿迁':'321300',
'拉萨':'540100',
'北京':'110100',
'贵港':'450800',
'七台河':'230900',
'象山':'330225',
'阿坝':'513200',
'郑州':'410100',
'直辖市':'110000',
'温州':'330300',
'晋中':'140700',
'果洛':'632600',
'松原':'220700',
'宁国':'341881',
'商丘':'411400',
'四会':'441284',
'大兴安岭':'232700',
'郴州':'431000',
'菏泽':'371700',
'枣庄':'370400',
'十堰':'420300',
'马鞍山':'340500',
'龙岩':'350800',
'成都':'510100',
'邢台':'130500',
'盐城':'320900',
'呼和浩特':'150100',
'本溪':'210500',
'宣城':'341800',
'哈尔滨':'230100',
'武威':'620600',
'肇庆':'441200',
'濮阳':'410900',
'吕梁':'141100',
'邵阳':'430500',
'安顺':'520400',
'西藏':'540000',
'南宁':'450100',
'宝鸡':'610300',
'邯郸':'130400',
'南昌':'360100',
'内蒙古':'150000',
'崇左':'451400',
'南昌县':'360121',
'宜宾':'511500',
'辽阳':'211000',
'林芝':'542600',
'江门':'440700',
'瑞安':'330381',
'乌兰察布':'150900',
'昭通':'530600',
'南京':'320100',
'武安':'130481',
'黄山':'341000',
'庆阳':'621000',
'泰安':'370900',
'云浮':'445300',
'大庆':'230600',
'如东':'320623',
'海安':'320621',
'芜湖':'340200',
'随州':'421300',
'南通':'320600',
'海南藏族':'632500',
'湖北':'420000',
'六安':'341500',
'南充':'511300',
'鹤壁':'410600',
'株洲':'430200',
'赣州':'360700',
'辽源':'220400',
'天水':'620500',
'衢州':'330800',
'贺州':'451100',
'四川':'510000',
'承德':'130800',
'赤峰':'150400',
'黑河':'231100',
'德州':'371400',
'高邮':'321084',
'仪征':'321081',
'荆门':'420800',
'临沂':'371300',
'句容':'321183',
'扬中':'321182',
'遵义':'520300',
'珠海':'440400',
'山东':'370000',
'海南':'460000',
'铜川':'610200',
'大连':'210200',
'三明':'350400',
'阳江':'441700',
'眉山':'511400',
'楚雄':'532300',
'禹州':'411081',
'长葛':'411082',
'太原':'140100',
'上饶':'361100',
'瓦房店':'210281',
'镇江':'321100',
'庄河':'210283',
'保山':'530500',
'防城港':'450600',
'遂宁':'510900',
'如皋':'320682',
'浙江':'330000',
'延吉':'224001',
'阿里':'542500',
'许昌':'411000',
'阿拉善盟':'152900',
'伊春':'230700',
'三门峡':'411200',
'武汉':'420100',
'蚌埠':'340300',
'连云港':'320700',
'忻州':'140900',
'吉安':'360800',
'白银':'620400',
'亳州':'341600',
'绥化':'231200',
'聊城':'371500',
'新乡':'410700',
'青岛':'370200',
'舟山':'330900',
'漳州':'350600',
'湘潭':'430300',
'张家口':'130700',
'茌平':'371523',
'乌海':'150300',
'济南':'370100',
'西安':'610100',
'鞍山':'210300',
'定州':'130682',
'泉州':'350500',
'山西':'140000',
'河池':'451200',
'安溪':'350524',
'惠安':'350521',
'海口':'460100',
'安达':'231281',
'孝感':'420900',
'六盘水':'520200',
'海城':'210381',
'禹城':'371482',
'汕头':'440500',
'泰州':'321200',
'晋江':'350582',
'南安':'350583',
'黄南':'632300',
'清远':'441800',
'那曲':'542400',
'漯河':'411100',
'广元':'510800',
'衡水':'131100',
'杭州':'330100',
'玉溪':'530400',
'钦州':'450700',
'佳木斯':'230800',
'银川':'640100',
'阳朔':'450321',
'新疆':'650000',
'乌鲁木齐':'650100',
'昌吉':'652300',
'中卫':'640500',
'吴忠':'640300',
'哈密尔顿':'14607',
'通化':'134100',
'中国':'0',
'伊犁':'650001',
'克拉玛依':'650002',
'哈密':'650003',
'塔城':'650004',
'喀什':'650005',
'阿克苏':'650006',
'石河子':'650007',
'五家渠':'650008',
'阿拉尔':'650009',
'图木舒克':'650012',
'巴音郭楞':'650010',
'吐鲁番':'650011',
'台湾':'710000',
'台北':'710100',
'新北':'710200',
'桃园':'710300',
'台中':'710400',
'台南':'710500',
'高雄':'710600',
'香港澳门':'810000',
'香港':'810100',
'澳门':'910100',
'雄安':'131200',
'宣化':'132100',
'阳原':'132200',
'尚义':'132300',
'沽源':'132400',
'万全':'132500',
'昆山':'3320100',
'江阴':'332020',
'张家港':'333020',
'常熟':'334020',
'丹阳':'335020',
'海门':'337020',
'溧阳':'338020',
'启东':'339020',
'邳州':'341020',
'东台':'343020',
'龙口':'372100',
'即墨':'372200',
'胶州':'372300',
'荣成':'372400',
'诸城':'372500',
'肥城':'372600',
'新泰':'372700',
'邹城':'373000',
'义乌':'331101',
'慈溪':'331112',
'诸暨':'331113',
'温岭':'331114',
'乐清':'331115',
'平湖':'331117',
'东阳':'331118',
'永康':'331423',
'冲绳':'00113',
'孟买':'02227',
'加尔各答':'02228',
'班加罗尔':'02229',
'加德满都':'02015',
'爱丽丝泉':'14509',
'柏斯':'14510',
'凯恩斯':'14511',
'帕塔亚':'01070',
'赫尔加达':'09108',
'哥伦比亚':'187',
'波哥大':'18701',
'亚特兰大':'16210',
'新加坡':'01417',
'迈阿密':'16211',
'达拉斯':'16212',
'爱民顿':'16310',
'海参崴':'05509',
'斯里巴加湾':'01105',
'萨尔茨堡':'06002',
'圣马力诺':'08607',
'庞贝':'08409',
'圣托里尼':'08004',
'伊拉克利翁':'08005',
'奥林匹亚':'08006',
'法兰克福':'06216',
'科隆':'06217',
'英格堡':'06510',
'琉森':'06511',
'摩纳哥城':'07302',
'安特卫普':'06902',
'戛纳':'07022',
'艾克斯':'07023',
'阿姆斯特丹':'07113',
'鹿特丹':'07114',
'平阴':'37101',
'太仓':'332120',
'蒙哥马利':'16213',
'朱诺':'16214',
'凤凰城':'16215',
'钱德勒':'16216',
'小石城':'16217',
'萨克拉曼多':'16218',
'长滩':'16219',
'丹佛':'16220',
'哈特佛特':'16221',
'多佛':'16222',
'塔拉哈希':'16223',
'檀香山':'16224',
'波易士':'16225',
'春田':'16226',
'印第安纳波里':'16227',
'第蒙':'16228',
'托派卡':'16229',
'巴顿鲁治':'16230',
'新奥尔良':'16231',
'奧古斯塔':'16232',
'亚纳波里':'16233',
'兰辛':'16234',
'底特律':'16235',
'杰克逊县':'16236',
'杰斐逊':'16237',
'赫勒那':'16238',
'林肯':'16239',
'卡逊城':'16240',
'康科德':'16241',
'特伦顿':'16242',
'圣菲':'16243',
'奥尔巴尼':'16244',
'水牛城':'16245',
'罗切斯特':'16246',
'洛利':'16247',
'俾斯麦':'16248',
'哥伦布':'16249',
'辛辛那提':'16250',
'克利夫兰':'16251',
'奥克拉荷马':'16252',
'塞伦':'16253',
'波特兰':'16254',
'哈立斯堡':'16255',
'巴尔的摩':'16256',
'普罗维登斯':'16257',
'皮尔':'16258',
'纳什维尔':'16259',
'奥斯汀':'16260',
'圣安东尼':'16261',
'盐湖城':'16262',
'蒙特利埃':'16263',
'列治文':'16264',
'西雅图':'16265',
'查尔斯顿':'16266',
'麦迪逊':'16267',
'夏延':'16268',
'肥东':'3401220',
'仁怀':'520380',
'盘州':'520220',
'孝义':'141180',
'贵溪':'360680',
'永城':'411480',
'库尔勒':'652801',
'建湖':'3209250',
'桓台':'3703210',
'拉斯维加斯':'091988',
'南苏丹':'SSD',
'朱巴':'SSD01',
'晋州':'130183',
'旬邑':'610120',
'珀勒德布尔':'02016',
'海盐':'330401',
'伊宁':'650101',
'单县':'371720',
'曹县':'371710',
'辛集':'130101',
'惠东':'441301',
'开平':'440701',
'中牟':'410101',
'阳谷':'371501',
'青县':'130901',
'江油':'510701',
'项城':'411601',
'蛟河':'220201',
'邵东':'430501',
'尤溪':'350401',
'江源':'220601',

}


def get_header():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }


def get_developer():
    return DEVELOPER.get(BY)

def deal_area(area):
    area = area.replace('市', '')
    area = area.replace('新疆维吾尔自治区', '新疆')
    area = area.replace('宁夏回族自治区', '宁夏')
    area = area.replace('广西壮族自治区', '广西')
    area = area.replace('内蒙古自治区', '内蒙古')
    area = area.replace('西藏自治区', '西藏')
    area = area.replace('自治区', '')
    if area != '吉林省':
        area = area.replace('省', '')
    return area


def get_fun_num():
    return FUN_AND_NUM.get(FUN_BIG_DATA)
import time
def get_time():
    hms = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return hms

if __name__ == '__main__':
    pass
