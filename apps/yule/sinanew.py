# 安装 pip3 install BeautifulSoup4 
#pip3 install requests
# pip install jupyter notebook
'用BeautifulSoup可以将网页信息转换为可操作物块'
'''
Pandas是Python的一个数据分析包，该工具为解决数据分析任务而创建。
Pandas纳入大量库和标准数据模型，提供高效的操作数据集所需的工具。
Pandas提供大量能使我们快速便捷地处理数据的函数和方法。
Pandas是字典形式，基于NumPy创建，让NumPy为中心的应用变得更加简单。
'''
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'sinanew souhu sina module'

__author__  ='LMQ'
# 获取新闻的标题，内容，时间和评论数
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
# import pandas

headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def getSohuYule(url):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
  }
    # YuleSource='https://v2.sohu.com/integration-api/mix/region/131?size=25&adapter=pc&secureScore=50&page={}&callback=jQuery1111'
    YuleSource = url 
    # YuleList =[]
    YuleListData = ''
    for i in range(1,3):
        res = requests.get(YuleSource.format(i),headers=headers)
        YuleListData= res.text.strip()
        YuleListData=YuleListData.lstrip('/**/jQuery1111(')
        YuleListData=YuleListData.rstrip(');')
        YuleListData = json.loads(YuleListData)
        #YuleList.extend(json.loads(YuleListData))
    return YuleListData

def getSohuYuleDetail(durl):
     res = requests.get(durl)
     res.encoding = 'utf-8'
     soup = BeautifulSoup(res.text,'html.parser')
     # print(title)
     if len(soup.select('.title-info-title')) == 0:
        title=soup.select('.text-title h1')[0].text
     else:
        title=soup.select('.title-info-title')[0].text.strip()
     article=soup.select('#mp-editor')
     detaills={"title":title,"article":article}
     return detaills   

def getSohuYuleDetailPicture (durl):
     #print(durl)
     res = requests.get(durl,headers=headers)
     res.encoding = 'utf-8'
     soup = BeautifulSoup(res.text,'html.parser')
     # print(title)
     if len(soup.select('#article-title-hash')) == 0:
        title='图片集合'
     else:
        title=soup.select('#article-title-hash')[0].text.strip()
     imgUrlList=soup.select('.scroll img')
     imgUrlTitle=soup.select('.pic-explain .txt p')
     #print(imgUrlTitle)
     #print(imgUrlList)
     imgDict={}
     imglen =0
     while imglen<len(imgUrlList):
         dit={imglen:{'title':str(imgUrlTitle[imglen]),'url':str(imgUrlList[imglen])}}
         imgDict.update(dit)
         imglen+=1
     # DetailPicture={"title":title,"imgUrlTitle":imgUrlTitle,"imgUrlList":imgUrlList}
     DetailPicture={"title":title,"imgs":imgDict}
     return DetailPicture 

def getNewsdetial(newsurl):
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    #找到标题
    newsTitle = soup.select('h1.main-title')[0].text.strip()
    #print(newsTitle)
    #nt = datetime.strptime(soup.select('.time-source')[0].contents[0].strip(),'%Y年%m月%d日%H:%M')
    #print(soup.select('span.date')[0].contents[0].strip())
    # 
    nt = datetime.strptime(soup.select('span.date')[0].contents[0].strip(),'%Y年%m月%d日 %H:%M')
    newsTime = datetime.strftime(nt,'%Y-%m-%d %H:%M')
    #获取文章内容
    newsArticle = getnewsArticle(soup.select('.article p'))
    newsAuthor = newsArticle[-1]
    return newsTitle,newsTime,newsArticle,newsAuthor
#处理文章内容    
def getnewsArticle(news):
    newsArticle = []
    for p in news:
         newsArticle.append(p.text.strip())
    return newsArticle

# 获取评论数量
def getCommentCount(newsurl):
    m = re.search('doc-i(.+).shtml',newsurl)
    newsid = m.group(1)
    #commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    commenturl = 'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-{}&group=0&compress=0&ie=utf-8&oe=utf-8&page=2&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1589009570794&_=1589009570794'
    comment = requests.get(commenturl.format(newsid))   #将要修改的地方换成大括号，并用format将newsid放入大括号的位置
    jd = json.loads(comment.text.lstrip('jsonp_1589009570794(').rstrip(')'))
    # print(jd)
    return jd['result']['count']['total']


def getNewsLinkUrl():
   # 得到异步载入的新闻地址（即获得所有分页新闻地址）
    #urlFormat = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1501000415111'
    urlFormat ='https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page={}&encode=utf-8&callback=feedCardJsonpCallback&_=1589002646872'
    url = []
    for i in range(1,2):
       # format可以将url里面的大括号（要修改的部分我们把它删去并换成大括号）换为我们要加入的值（如上面代码中的 i）
        res = requests.get(urlFormat.format(i))
        #jd = json.loads(res.text.lstrip('  feedCardJsonpCallback(').rstrip(');'))
        #print('=')
        tempRes=res.text.strip()
        tempRes=tempRes.lstrip('try{feedCardJsonpCallback')
        tempRes=tempRes.lstrip('(')
        tempRes=tempRes.rstrip('};')
        tempRes=tempRes.rstrip('catch(e){')
        tempRes=tempRes.rstrip(';}')
        tempRes=tempRes.rstrip(')')
        #print(tempRes)
        jd = json.loads(tempRes)
        # 查找到url地址
        url.extend(getUrl(jd))     #entend和append的区别
    return url

def getUrl(jd):
#     获取每一分页的新闻地址
    url = []
    for i in jd['result']['data']:
        url.append(i['url'])
    return url

# 取得新闻时间，编辑，内容，标题，评论数量并整合在total_2中
def getNewsDetial():
    title_all = []
    author_all = []
    commentCount_all = []
    article_all = []
    time_all = []
    url_all = getNewsLinkUrl()
    for url in url_all:
        title_all.append(getNewsdetial(url)[0])
        time_all.append(getNewsdetial(url)[1])
        article_all.append(getNewsdetial(url)[2])
        author_all.append(getNewsdetial(url)[3])
        commentCount_all.append(getCommentCount(url))
    total_2 = {'a_title':title_all,'b_article':article_all,'c_commentCount':commentCount_all,'d_time':time_all,'e_editor':author_all}
    return total_2



# ( 运行起始点 )用pandas模块处理数据并转化为excel文档
#df = pandas.DataFrame(getNewsDetial())
#df.to_excel('news2.xlsx')


#if __name__ == "__main__":
    #getSohuYuleDetailPicture('https://www.sohu.com/picture/412779106?scm=1002.280027.0.0-0&spm=smpc.ch19.fd.19.1597281808871Sj40oJy')
  
 
