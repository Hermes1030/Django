from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    # 通常是一个用于生成友好URL的短标签或别名
    slug = models.SlugField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
