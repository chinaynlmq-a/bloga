from django.db import models

# Create your models here.
class MwArticleList(models.Model):
  title = models.CharField('文章标题',max_length=60)
  detailurl = models.URLField('详细页面地址',max_length=8182)
  description = models.TextField('文章简短描述',help_text='展示文章内容提要')
  
  class Meta:
    verbose_name = '采集美文阅读网'
    ordering =['id']
  
  # 返回改实例对像对名字
  def __str__(self):
    return self.title  


