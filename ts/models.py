from django.db import models

class Url(models.Model):
    short_url = models.CharField(max_length=40)
    long_url = models.URLField('URL', unique=True)