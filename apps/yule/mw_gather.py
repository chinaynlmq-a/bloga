
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'采集美文网址模版'
__author__  ='LMQ'
import os
import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
# import enumerate

# from models import MwArticleList
# BASE_DIR = os.path.dirname(os.getcwd())
# # 设置工作目录，使得包和模块能够正常导入 自定义模版可以正常导入
# sys.path.append(BASE_DIR)
# from django.conf import settings
# settings.configure()
# import os,django
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# django.setup()



class mw:
    def __init__(self,usrHost='https://www.52ycw.com'):

        self.headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

        self.urlHost= usrHost
    
    #获取列表分页地址url 需要获取page分页的总数 
    def getListLinkUrl(self,url,page):
        urls=[]
        for i in range(1,page):
            urls.append(url.format(i))
        return urls

    # 获取详细页面链接地址    
    def getListContent(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        listHtml=soup.select('.list-l .lists')
        listContent = self.listContent(listHtml)
        return listContent    
        
    def listContent(self,listContent):  
        # titles=[]
        # detailurls=[]
        descriptions =[]
        for tit in listContent:
            tit.find('p').a.decompose()
            defas={
                'title': tit.find('h3').text.strip(),
                'detailurl':('%s%s' % (self.urlHost,tit.find('a').attrs['href'])),
                'description':tit.find('p').text.strip()
            }
            # detailurls.append('%s%s' % (self.urlHost,tit.find('a').attrs['href']))
            # titles.append(tit.find('h3').text.strip())
            # tit.find('p').a.decompose()
            # descriptions.append(tit.find('p').text.strip())
            descriptions.append(defas)
        return descriptions

    def run(self):
        pass


if __name__ == "__main__":
    listUrl=mw().getListLinkUrl('https://www.52ycw.com/aqmw/list_5_{}.html',3)
    for url in listUrl:
         temp = mw().getListContent(url)
        #  print(temp)
         for o in temp:
             print(o)    
             print('====')
         #temp=mw().getListContent(url)[0]
         #for name in temp:
