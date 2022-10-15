from django.forms import Form
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import *


class MainModelForm(forms.Form):
    language = forms.ModelChoiceField(queryset=LanguageSet.objects.all())
    url = forms.CharField(max_length=200)


