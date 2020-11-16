from django.db import models

# Create your models here.

class Article (models.Model):
    category = models.CharField(max_length=350, blank=False, default='')
    article_url = models.CharField(max_length=350, blank=False, default='')
    subcat_name = models.CharField(max_length=350, blank=False, default='')
    page_name = models.CharField(max_length=350, blank=False, default='')
    article_writer = models.CharField(max_length=350, blank=False, default='')
    article_time = models.CharField(max_length=350, blank=False, default='')
    article_title = models.CharField(max_length=1350, blank=False, default='')
    article_caption = models.CharField(max_length=1350, blank=False, default='')
    article_txt = models.CharField(max_length=2000, blank=False, default='')
