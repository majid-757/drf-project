from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


from .models import Article


class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)



class ArticleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(Article.objects.filter(status=True), 
        pk=self.kwargs.get("pk"))



class UserView(ListView):
    context_object_name = 'user_list'

    template_name = 'blog/auth/user_list.html'

    queryset = User.objects.all()

    # def get_queryset(self):
    #     return User.objects.all()



