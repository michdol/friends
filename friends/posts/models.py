from django.db import models


class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
