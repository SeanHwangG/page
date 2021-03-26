from django.shortcuts import render
from .models import GitBook


def home(request):
  context = {'gitbooks': GitBook.objects.all()}
  return render(request, 'gitbook/home.html', context)
