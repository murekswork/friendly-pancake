from django.db import models
from django.urls import reverse


class LanguageSet(models.Model):
    language_ab = models.CharField(max_length=3, default='RU', verbose_name='language_abbreviation')
    language = models.CharField(max_length=100, default='RUSSIAN', verbose_name='full_language')

    def __str__(self):
        return self.language


class MainModel(models.Model):
    url = models.CharField(max_length=200, verbose_name='URL')
    language = models.CharField(max_length=10, verbose_name='language')

    def __str__(self):
        return 'MainFormObject'


    def get_absolute_url(self):
        return reverse('home')

# Create your models here.
