from django.db import models


class User(models.Model):
    login = models.CharField(max_length=16)
    passwrod = models.CharField(max_length=16)
    username = models.CharField(max_length=16)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Publication(models.Model):
    title = models.CharField(max_length=16)
    text_content = models.CharField(max_length=16)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

    def __str__(self):
        return self.title