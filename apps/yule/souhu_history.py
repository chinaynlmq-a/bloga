
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
import souhu_model
headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def getShHistoryList(num=1):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
   }
    WySource='https://v2.sohu.com/integration-api/mix/region/6282?size=25&adapter=pc&secureScore=50&page={}&pvId=1597977513986eN9F3Iu&requestId=191031134648Z27H_1597977563584&callback=jQuery11240'
    WySource=WySource.format(num)
    #YuleSource = url 
    # YuleList =[]
    WyBabyList = ''
    res = requests.get(WySource,headers=headers)
    WyBabyList= res.text.strip()
    WyBabyList=WyBabyList.lstrip('data_callback(')
    WyBabyList=WyBabyList.rstrip(');')
    WyBabyList = json.loads(WyBabyList)
    #YuleList.extend(json.loads(YuleListData))
    return WyBabyList

def getWyBabyListDetail(durl):
     res = requests.get(durl)
     res.encoding = 'gbk'
     soup = BeautifulSoup(res.text,'html.parser')
     title=soup.select('#epContentLeft h1')[0].text.strip()
     time_source=soup.select('.post_time_source')[0].text.strip()
     article=soup.select('.post_body .post_text') 
     detaills={"title":title,'time_source':time_source,"article":article}
     return detaills   

if __name__ == "__main__":
    #print(getWyBizList(2))
    # https://money.163.com/20/0819/07/FKCJDGA100259DLP.html
    #print(getWyBizListDetail('https://money.163.com/20/0819/07/FKCJDGA100259DLP.html'))
    
    print(souhu_model.GetSouhu().get_list())
