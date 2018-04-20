import re
#xpath提取不出url,使用正则
def extract_url(url,result):
    us = []
    if url == 'http://www.wenwuchina.com/article/MmArticle/getList.do':
        result1 = re.findall(r'"art_id":(.*?),.*?"aUrl":(.*?),', result)
        for info, info1 in result1:
            us.append('http://www.wenwuchina.com/article/' + str(info1) + '/' + str(info) + '.html')

    elif url == 'http://www.sach.gov.cn/col/col8/index.html' or url == 'http://www.sach.gov.cn/col/col722/index.html':
        result1 = re.findall(r"href='(/art.*?tml)", result)
        for info in result1:
            us.append('http://www.sach.gov.cn' + info)

    elif url == 'http://www.gzmuseum.com/zx/gbdt/':
        result1 = re.findall(r'(http://www.gzmuseum.com/zx/gbdt/20.*?)"', result)
        for info in result1:
            us.append(info)

    elif url == 'http://www.gzmuseum.com/zx/zxxx/':
        result1 = re.findall(r'(http://www.gzmuseum.com/zx/zxxx/20.*?)"', result)
        for info in result1:
            us.append(info)

    elif url == 'http://api.bjartmuseum.com/interface/museum/bjww':
        result1 = re.findall(r'www.bjww.gov.cn(http.*?tml)', result)
        for info in result1:
            us.append(info)

    elif url == 'http://www.gansumuseum.com/vm_bwg/list_wzxx.aspx?_lmid1=a28263f4-ad42-4ae9-9d27-8ee92e025e04&_lmbh1=008&_lmmc1=%d0%c2%ce%c5&_lmid2=32727ec9-4f62-4d20-bc43-0715aac04f77&_lmbh2=008002&_lmmc2=%ce%c4%b2%a9%b6%af%cc%ac&_lmid3=&_lmbh3=&_lmmc3=&_=c6d622791c994eefb29a5eafb7a9cca4':
        result1 = re.findall(r"a href='\.\.(.*?)'", result)
        for info in result1:
            us.append('http://www.gansumuseum.com' + info)

    elif url == 'http://jsswwj.jiangsu.gov.cn/col/col12967/index.html' or url == 'http://jsswwj.jiangsu.gov.cn/col/col12794/index.html':
        result1 = re.findall(r"href='(/art.*?tml)", result)
        for info in result1:
            us.append('http://jsswwj.jiangsu.gov.cn' + info)
    return us
#提出url有问题,处理url
def filter_url(url,urllist):
    if url == 'http://www.hainanmuseum.org/xwdt/?tag_id=1':
        for num in range(len(urllist)):
            urllist[num] = urllist[num].replace('/xwdt', '', 1)


    elif url == 'http://www.gsww.gov.cn/Web_List.aspx?ClsID=26':
        for num in range(len(urllist)):
            urllist[num] = urllist[num].replace(' ', '')

    return urllist
#过滤标题
def filter_title(area, text_f, title):
    if text_f == '江苏文物局':
        title = title.split()[-1]
    return title
#过滤内容
def filter_cont(area,text_f,content):
    if text_f == '国家博物馆':
        content = re.sub('.*相关资讯[\s|\S]*', '', content)
    elif text_f == '中国美术家协会':
        content = re.sub('<h3[\s|\S]*?</p>', '', content)
    elif text_f == '浙江省博物馆':
        content = re.sub('<div>[\s|\S]*发布时间.*', '<div>', content)
        content = re.sub('<img.*?fav.png.*?>', '', content)
    elif text_f == '国家文物局':
        content = re.sub('<img  id="loading".*?>', '', content)
    elif text_f == '新浪收藏':
        content = re.sub('.*获取更多资.*', '', content)
    elif text_f == '北京文艺网':
        content = re.sub('<h1>[\s|\S]*?ckepop[\s|\S]*?<div>', '<div>', content)
        content = re.sub('.*本网发表的所有内容[\s|\S]*', '</div>', content)
    elif text_f == '光明网书画频道':
        content = re.sub('<span.*pagefontcon.*', '</div></p></center>', content)
    elif text_f == '凤凰网河南':
        content = re.sub('<span class="ifengLogo">.*204c433878d5cf9size1_w16_h16.*/span>', '', content)

    return content
#过滤内容样式
def filter_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', htmlstr)
    # 去掉h和style标签
    s = re.sub(r'<style>[\s.\S]*?</style>', '', s)
    # 替换div
    s = re.sub(r'<div.*?>', '<div>', s)
    # 替换img属性
    s = re.sub(r'img_width="\d+"', '', s)
    s = re.sub(r'img_height="\d+"', '', s)
    s = re.sub(r'height="\d+"', '', s)
    s = re.sub(r'width="\d+"', '', s)
    s = re.sub(r'style=".*?"', '', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    # 去掉input标签
    s = re.sub(r'<input.*?>', '', s)
    return s

