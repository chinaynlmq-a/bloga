
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'搜狐  module'

__author__  ='LMQ'
# 获取搜狐 的标题，内容
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

from storm.models import Category,Tag,Keyword,Article
from user.models import Ouser
import random
from user.webtools import auto_article_url

HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
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
        _jsonp= self.__get_requests(url=WySource,tag='2',encode='utf-8')
        # shList=shList.lstrip('/**/')
        # shList=shList.lstrip(callback)
        # shList=shList.lstrip('(')
        # shList=shList.rstrip(');')
        # shList = json.loads(shList)
        try:
          return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
        except:
          #raise ValueError('Invalid Input') 
          return {}
        #return shList

    # 处理 统一的请求地址，返回soup 对象
    def __get_requests(self,url,tag='1',encode='utf-8'):
     res = requests.get(url,headers=self._headers)
     res.encoding = encode
     if tag == '1':
       soup = BeautifulSoup(res.text,'html.parser')
       return soup
     soup = res.text 
     return soup

    def get_detail(self,durl):
     soup = self.__get_requests(durl)
     if len(soup.select('.title-info-title')) == 0:
        title=soup.select('.text-title h1')[0].text
     else:
        title=soup.select('.title-info-title')[0].text.strip()
     article=soup.select('#mp-editor p')
     content = self.get_detailp_1(article[1:len(article)-2])
     # 最后一条
     tem = article[-2:-1]
     temp_p =BeautifulSoup(str(tem[0]),'html.parser')
     # 获取a标签到到上一个兄弟节点
     if temp_p.a == None:
       temp_p=''
     else:
       temp_p=temp_p.a.previous_sibling
     #article=article[:len(article)-1]
     content.append('<p class="ql-align-justify">'+temp_p+'</p>')
     detaills={"title":title,"article":content}
     return detaills
     
    def getDetailPicture (self,url,encode='utf-8'):
        soup = self.__get_requests(url)
        if len(soup.select('#article-title-hash')) == 0:
            title='图片集合'
        else:
            title=soup.select('#article-title-hash')[0].text.strip()
        imgUrlList=soup.select('.scroll img')
        imgUrlTitle=soup.select('.pic-explain .txt p')
        imgDict={}
        imglen =0
        while imglen<len(imgUrlList):
            dit={imglen:{'title':str(imgUrlTitle[imglen]),'url':str(imgUrlList[imglen])}}
            imgDict.update(dit)
            imglen+=1
        DetailPicture={"title":title,"imgs":imgDict}
        return DetailPicture 

    def get_detailp_1(self,p_arr):
      plist=[]
      for p in p_arr:
        plist.append(str(p))
      return plist
    
'''
 需求：运行 save_article 方法 保存文章内容
 1.获取文章列表
 2.获取分类 一级和二级
 3.获取描述
 4.关键字
 5.详细内容处理
 6.保存到数据库 
'''
class Sina:
  def __init__(self):
    pass
  def get_list_url(self):
    url = 'https://interface.sina.cn/games/gpapi/2016index/2020_interface_game_pc_home_newslist.shtml?callback=jQuery17025633626432682677_1599635456353&fid=1_1&page=1&pageSize=20&_=1599635622569'
    jsonp=get_html_content(url,tag='2')
    data=get_jsonp_data(jsonp)
    if data.exists():
      tempSoup=BeautifulSoup(str(data.data),'html.parser')
      print(tempSoup)
    else:
      return {'err':'sss'}
  def get_detail(self):
    pass
  def save_article(self):
    # 作者
    author = Ouser.objects.filter(username='testadmin')
    author=author.first()
    title = 'test1'
    # 描述
    summary ='test1'
    # 文章内容
    body ='test1'
    # 缩图
    img_link ='/ss1'
    views = auto_love()
    loves = auto_love()
    slug = auto_article_url()
    category= Category.objects.filter(name='最热资讯')
    category = category.first()
    # 多对多
    tag =Tag.objects.create(name='测试动态生1',slug=auto_article_url(),description='测试动态生描述1')
    # 多对多
    keyword =Keyword.objects.create(name='哈哈测试')
    if  Article.objects.filter(pk='1').exists():
      ar=Article.objects.filter(pk='1').update(author=author,title=title,summary=summary,body=body,img_link=img_link,views=views,slug=slug,loves=loves,category=category)
    else:
      ar=Article.objects.create(author=author,title=title,summary=summary,body=body,img_link=img_link,views=views,slug=slug,loves=loves,category=category)
      ar.tags.add(tag)
      ar.keywords.add(keyword)

    # ar=Article.objects.create(author=author,title=title,summary=summary,body=body,img_link=img_link,views=views,slug=slug,loves=loves,category=category)
    # ar.tags.add(tag)
    # ar.keywords.add(keyword)

def get_html_content(url,tag='1',encode='utf-8'):
     res = requests.get(url,headers=HEADERS)
     res.encoding = encode
     if tag == '1':
       soup = BeautifulSoup(res.text,'html.parser')
       return soup
     soup = res.text 
     return soup

def get_jsonp_data(_jsonp):
  try:
    return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
  except:
    return {}

def auto_love():
    num =''
    for i in range(2):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        num += ch 
    return num

if __name__ == "__main__":
  #print(GetSouhu().get_list('131'))
  print(Sina().get_list_url())
