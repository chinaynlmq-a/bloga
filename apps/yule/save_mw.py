from .models import MwArticleList
from .mw_gather import mw
def run():
  listUrl=mw().getListLinkUrl('https://www.52ycw.com/aqmw/list_5_{}.html',216)
  # temp=[]
  for url in listUrl:
      temp=mw().getListContent(url)
      for o in temp:
        MwArticleList.objects.create(**o)
        # print(o)
        # temp.append(o)
  #MwArticleList.objects.update_or_create(temp)      

