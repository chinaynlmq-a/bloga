
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'sinanew 网易 商业 module'

__author__  ='LMQ'
# 获取新闻的标题，内容，时间和评论数
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
class AutoSouceUrl:
    pass

def getWyBizList(num):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
  }
    if num <= 1:
        WySource='http://money.163.com/special/002557RF/data_idx_shangye.js?callback=data_callback'
    else:
        WySource='http://money.163.com/special/002557RF/data_idx_shangye_0{}.js?callback=data_callback' 
        WySource=WySource.format(num)

    #YuleSource = url 
    # YuleList =[]
    WyBizList = ''
    res = requests.get(WySource,headers=headers)
    WyBizList= res.text.strip()
    WyBizList=WyBizList.lstrip('data_callback(')
    WyBizList=WyBizList.rstrip(');')
    WyBizList = json.loads(WyBizList)
    #YuleList.extend(json.loads(YuleListData))
    return WyBizList

def getWyBizListDetail(durl):
     res = requests.get(durl)
     res.encoding = 'utf-8'
     soup = BeautifulSoup(res.text,'html.parser')
     title=soup.select('#epContentLeft h1')[0].text.strip()
     time_source=soup.select('.post_time_source')[0].text.strip()
     article=soup.select('.post_body .post_text') 
     detaills={"title":title,'time_source':time_source,"article":article}
     return detaills   

if __name__ == "__main__":
    #print(getWyBizList(2))
    # https://money.163.com/20/0819/07/FKCJDGA100259DLP.html
    print(getWyBizListDetail('https://money.163.com/20/0819/07/FKCJDGA100259DLP.html'))
 
