from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# 继承 AbstractUser ，django 自带用户类，扩展用户个人网站字段，用户头像字段
class Ouser(AbstractUser):
    # 扩展用户个人网站字段
    link = models.URLField('个人网址', blank=True, help_text='提示：网址必须填写以http开头的完整形式')
    # 扩展用户头像字段
    avatar = ProcessedImageField(
        upload_to='avatar/%Y/%m/%d',
        default='avatar/default.png',
        verbose_name='头像',
        processors=[ResizeToFill(80, 80)]
    )

    class Meta:
        verbose_name = '用户'  # 定义网站管理后台表名
        # 指定，模型的复数形式是什么 若未提供该选项, Django 会使用 verbose_name + "s".
        verbose_name_plural = verbose_name
        #这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的 降序
        ordering = ['-id']

    def __str__(self):
        return self.username

