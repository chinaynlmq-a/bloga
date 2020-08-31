
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'网易 module'
__author__  ='LMQ'
# 处理网易咨询列表和内容处理
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

class GetWY:
    def __init__(self):
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
    '''
        category
        100 亲子
        101 商业
        102 段子
    '''
    def getList(self,category='100',page=1):
        # 获取列表url
        url = self.checkUrl(category,page)
        List = ''
        res = requests.get(url,headers=self._headers)
        List= res.text.strip()
        List=List.lstrip('data_callback(')
        List=List.rstrip(');')
        List = json.loads(List)
        return List

    def _get_requests(self,url,encode='utf-8'):
     res = requests.get(url,headers=self._headers)
     res.encoding = encode
     soup = BeautifulSoup(res.text,'html.parser')
     return soup
    # 详细页面内容获取
    def getDetail(self,url,encode='utf-8'):
        soup = self._get_requests(url,encode)
        # 轮播图文章
        if soup.select('textarea'):
            are=soup.select('textarea')[0]
            are = are.text.strip()
            are = json.loads(are)
            #print(are.inf)
            return {"title":are['info']['setname'],'articlelist':are['list']}
        # 普通情况的文章    
        else:
            if len(soup.select('#epContentLeft')) <1:
                return {"four":'four'}
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
            article=self.get_list_str(allp_s)

            if te:
                article.append('<p>'+te+'</p')

        detaills={"title":title,'time_source':time_source,"article":article}
        return detaills   
    def get_list_str(self,p_arr):
        plist=[]
        for p in p_arr:
            plist.append(str(p))
        return plist
    # 获取不同的列表数据地址    
    def checkUrl(self,category,page):
        url = None
        if category == '100':
            if page <= 1:
                url = 'https://baby.163.com/special/003687OS/newsdata_hot.js?callback=data_callback'
            else:
                url = 'https://baby.163.com/special/003687OS/newsdata_hot_0{}.js?callback=data_callback'
                url=url.format(page)
            return url
        if category == '101':
            if page <= 1:
                url='http://money.163.com/special/002557RF/data_idx_shangye.js?callback=data_callback'
            else:
                url='http://money.163.com/special/002557RF/data_idx_shangye_0{}.js?callback=data_callback' 
                url=url.format(page)
            return url
        if category == '101':
            if page <= 1:
                pass
            else:
                pass
            return url         

if __name__ == "__main__":
    # print(GetWY().getDetail('https://baby.163.com/20/0831/09/FLBNISRR00367V0V.html','gbk')) 
    # print(GetWY().getDetail('https://money.163.com/20/0831/08/FLBJFFRI00259DLP.html')) 
    print(GetWY().getList('101')) 
 
