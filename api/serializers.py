from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.models import Article


    


class ArticleSerialiser(serializers.ModelSerializer):

    def get_author(self, obj):
        return {
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
            "username": obj.author.username,

        }

    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Article
        fields = "__all__"
        # exclude = ("created",)

    def validate_title(self, value):
        filter_list = ["javascript", "laravel", "PHP"]

        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("Don't use bad words! : {}".format(i))


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        



