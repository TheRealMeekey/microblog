from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = 'Текст поста'
        verbose_name_plural = 'Тексты постов'

    text = models.TextField(verbose_name='Текст сообщения')
