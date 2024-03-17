from django.db import models

class VideoLink(models.Model):
    url = models.URLField()
