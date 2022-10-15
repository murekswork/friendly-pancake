from django.core.exceptions import ValidationError
from django.http import *
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import MainModelForm


# class HomeView(FormView):
#     form_class = HomeForm
#     template_name = 'home.html'

def main_form(request):
    data = {}
    if request.method == 'POST':
        form = MainModelForm(request.POST)
        if form.is_valid():
            data['language'] = form.cleaned_data['language']
            data['url'] = form.cleaned_data['url']

    else:
        form = MainModelForm()
    return render(request, 'home.html', {'form': form})

# Create your views here.
