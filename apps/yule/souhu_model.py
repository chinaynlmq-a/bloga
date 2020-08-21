
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'搜狐 历史 module'

__author__  ='LMQ'
# 获取新闻的标题，内容，时间和评论数
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

class GetSouhu:
    def __init__(self):
        self._headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

    # 6282 历史
    # 131 娱乐 
    def get_list(self,category='6282',size=25,page=1,callback='jQuery11240'):
        WySource='https://v2.sohu.com/integration-api/mix/region/{}?size={}&adapter=pc&secureScore=50&page={}&pvId=1597977513986eN9F3Iu&requestId=191031134648Z27H_1597977563584&callback={}'

        # 动态获取url链接地址
        WySource=WySource.format(category,size,page,callback)
        res = requests.get(WySource,headers=self._headers)
        shList= res.text.strip()
        shList=shList.lstrip('/**/')
        shList=shList.lstrip(callback)
        shList=shList.lstrip('(')
        shList=shList.rstrip(');')
        shList = json.loads(shList)
        return shList

    # 处理 统一的请求地址，返回soup 对象
    def __get_requests(self,url,encode='utf-8'):
     res = requests.get(url)
     res.encoding = 'utf-8'
     soup = BeautifulSoup(res.text,'html.parser')
     return soup

    def get_detail(self,durl):
     soup = self.__get_requests(durl)
     if len(soup.select('.title-info-title')) == 0:
        title=soup.select('.text-title h1')[0].text
     else:
        title=soup.select('.title-info-title')[0].text.strip()
     article=soup.select('#mp-editor')
     detaills={"title":title,"article":article}
     return detaills
    

if __name__ == "__main__":
  print(GetSouhu().get_detail('https://www.sohu.com/a/414162242_100103848?spm=smpc.tag-page.fd-news.3.1597986862445ROid4Pf'))
