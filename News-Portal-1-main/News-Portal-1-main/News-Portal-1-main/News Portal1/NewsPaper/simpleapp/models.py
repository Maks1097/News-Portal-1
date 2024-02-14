from django.db import models
from datetime import datetime
from django.urls import reverse


class New(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICE = [
        (NEWS, 'Новости'),
        (ARTICLE, 'Статья')
    ]
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default='NW')

    description = models.TextField()

    news = models.TextField()

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )

    time_now = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()