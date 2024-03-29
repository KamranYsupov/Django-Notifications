from django.db import models

from news.models import News


class Notification(models.Model):
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_create']
