
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'sinanew 网易 亲子 module'

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

def getWyBabyList(num):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
  }
    if num <= 1:
        WySource='https://baby.163.com/special/003687OS/newsdata_hot.js?callback=data_callback'
    else:
        WySource='https://baby.163.com/special/003687OS/newsdata_hot_0{}.js?callback=data_callback' 
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
     if soup.select('textarea'):
         are=soup.select('textarea')[0]
         are = are.text.strip()
         are = json.loads(are)
         #print(are.inf)
         return {"title":are['info']['setname'],'articlelist':are['list']}
     else:
        title=soup.select('#epContentLeft h1')[0].text.strip()
        time_source=soup.select('.post_time_source')[0].text.strip()
        #article
        allp=soup.select('.post_body #endText')[0]
        # 转化为BeautifulSoup 对象处理html文件
        ss = BeautifulSoup(str(allp),'html.parser')
        # 获取divs个数
        divs = ss.select('p > div')
        divs_len = len(divs)
        te = None
        # 清除 div除了最后一个的内容
        for i,v in enumerate(divs):
            if(i>=divs_len-1):
                te = ss.div.div.text    
            ss.div.div.decompose()
        allp_s=ss.select('p')
        #print(ss.div.div)
        #ss.div.div.extract()
        #print(BeautifulSoup(allp[0].text,'html.parser')) 
        article=get_list_str(allp_s)

        if te:
            article.append('<p>'+te+'</p')

     detaills={"title":title,'time_source':time_source,"article":article}
     return detaills   

# 获取并重组list返回list字符串
def get_list_str(p_arr):
    plist=[]
    for p in p_arr:
        plist.append(str(p))
    return plist

if __name__ == "__main__":
    #print(getWyBizList(2))
    # https://money.163.com/20/0819/07/FKCJDGA100259DLP.html
    #print(getWyBizListDetail('https://money.163.com/20/0819/07/FKCJDGA100259DLP.html'))
    print(getWyBabyListDetail('https://baby.163.com/20/0831/09/FLBNISRR00367V0V.html')) 
