from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32)
    text_content = models.CharField(max_length=1024)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('CategoryForArticle', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CategoryForArticle(models.Model):
    category_name = models.CharField(max_length=32, db_index=True)

    def __str__(self):
        return self.category_name


class LikeForArticle(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
