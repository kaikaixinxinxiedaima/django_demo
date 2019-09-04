from django.db import models

# Create your models here.

class Article(models.Model):
    #唯一ID
    article_id = models.AutoField(primary_key=True)

    #文章标题
    title = models.TextField(max_length=100)

    #文章摘要
    brief_content = models.TextField(max_length=200)

    #文章内容
    content = models.TextField(max_length=2000)

    #文章发布日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
