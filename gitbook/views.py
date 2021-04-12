from django.shortcuts import render
from .models import Gitbook


def home(request):
  context = {'markdowns': Gitbook.objects.all()}
  return render(request, 'markdown/home.html', context)
