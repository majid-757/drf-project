from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.models import Article


class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ("created",)




class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        



