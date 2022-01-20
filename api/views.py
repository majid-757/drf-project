from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.shortcuts import render

from blog.models import Article
from .serializers import ArticleSerialiser



class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser










