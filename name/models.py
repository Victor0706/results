from django.contrib.auth.models import User
from django.urls import reverse

from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    type = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'торговцы'),
        ('gildemaster', 'гилдмастеры'),
        ('quest', 'квестгиверы'),
        ('smith', 'кузнецы'),
        ('tanner', 'кожевники'),
        ('potion', 'зельевары'),
        ('spellmaster', 'мастера заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    text = models.TextField()
    category = models.CharField(max_length=16, choices=type, default='tank')
    upload = models.FileField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    CONSIDERATION = 'CN'
    ACCEPTED = 'AC'
    REMOVED = 'RM'
    CATEGORY_CHOISES = (
        (CONSIDERATION, 'Рассмотрение'),
        (ACCEPTED, 'Принято'),
        (REMOVED, 'Удалено'),
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOISES, default=CONSIDERATION)

    def __str__(self):
        return f'{self.text[:20]}'

    def get_absolute_url(self):
        return reverse('response_list')


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

