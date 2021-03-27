from django.shortcuts import render
from .models import Markdown


def home(request):
  context = {'markdowns': Markdown.objects.all()}
  return render(request, 'markdown/home.html', context)
