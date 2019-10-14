from django.db import models

class CrawledItem(models.Model):
    author_handle = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    tags = models.TextField()
    copy = models.TextField()
    status = models.IntegerField()