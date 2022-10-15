from django.contrib import admin
from django.urls import path, include
from .views import main_form

urlpatterns = [
    path('', main_form, name='home'),
]