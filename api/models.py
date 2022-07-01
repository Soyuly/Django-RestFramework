from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)