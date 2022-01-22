from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from django.shortcuts import render
from django.contrib.auth.models import User


from blog.models import Article
from .serializers import ArticleSerialiser, UserSerialiser



class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser



class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
   

class ArticleUpdate(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser


class ArticleDelete(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser












class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser



class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser





