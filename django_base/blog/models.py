from django.db import models

# Create your models here.
class BlogK(models.Model):
    # 博客标题
    title=models.CharField(max_length=150)
    # 博客正文
    body=models.TextField()
    # 博客创建时间
    create_date=models.DateTimeField()
    