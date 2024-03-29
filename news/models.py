from django.contrib.auth import get_user_model
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', db_index=True)
    content = models.TextField(verbose_name='Контент', blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор'
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Новости'
        verbose_name_plural = 'Новость'

    def __str__(self):
        return self.title
