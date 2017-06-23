# -*- coding: utf-8 -*-
import requests
import json
from lxml import etree

'''
1、requst：构建请求
'''
url = r"http://www.kankanwu.com/Action/anshajiaoshibiyepian/"
html = requests.get(url)
html.encoding = 'utf-8'

url = r"http://www.kankanwu.com/Action/anshajiaoshibiyepian/"
html = requests.post(url);
html.encoding = 'utf-8'

url = r"http://www.kankanwu.com/index.php?s=Showlist-show-id-2-mcid--lz--area--year--letter--order-addtime-picm-1-p-242"
html = requests.get(url)
html.encoding = 'utf-8'


'''
2、下载文件
'''
url = r"http://img.netbian.com/file/2017/0412/ac6f8471e854361c105e98718b77d2f4.jpg"
html = requests.get(url,stream=True)
for img in html.iter_content(chunk_size=100):
    print len(img)

'''
3、html文件后处理
'''
res = etree.HTML(html.text)
title = res.xpath(r'''//*[@id="contents"]/li''')
for item in title:
    head = item.xpath(r'''./div/h3/a''')[0].text
    actors = [x.text for x in item.xpath(r'''./div/p[1]/a''')]
    types = [x.text for x in item.xpath(r'''./div/p[2]/a''')]
    coverImg = item.xpath('''./a/img''')[0].get("src")
    print json.dumps({ "head": head, "actors": actors, "type": types, "coverImg": coverImg}, ensure_ascii=False)




