from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Article


class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ("created",)




class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        



