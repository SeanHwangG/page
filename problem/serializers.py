from rest_framework import serializers

from problem.models import Problem


class ProblemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Problem
    fields = '__all__'

  def to_representation(self, instance):
    data = super().to_representation(instance)
