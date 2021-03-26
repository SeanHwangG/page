from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
  exclude = []

  class Meta:
    model = User
    fields = '__all__'

  def to_representation(self, instance):
    data = super().to_representation(instance)
