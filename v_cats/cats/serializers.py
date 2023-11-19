from rest_framework import serializers
from .models import Cats
from django.contrib.auth.models import User


class CatsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cats
        fields = '__all__'# ["name", "age", "breed", "hairiness", "user"]


class UserSerializer(serializers.ModelSerializer):
    all_cats = CatsSerializer(source='cats', many=True)

    class Meta:
        model = User
        fields = ["username", "all_cats"]
