from rest_framework import viewsets, serializers
from rest_framework.generics import ListAPIView
from problem.serializers import ProblemSerializer
from django.shortcuts import render
from problem.models import Problem
from .models import Problem


def home(request):
  context = {'problems': Problem.objects.all()}
  return render(request, 'problem/home.html', context)


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
  def post(self, problem):
    return Problem.objects.create(**problem)


class ProblemViewSet(viewsets.ModelViewSet):
  queryset = Problem.objects.all().order_by('problem_id')
  serializer_class = ProblemSerializer


class ProblemList(ListAPIView):
  queryset = Problem.objects.all()
  serializer_class = ProblemSerializer
