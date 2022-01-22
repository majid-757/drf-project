from django.urls import path, include

from .views import ArticleList, ArticleDetail, UserView

app_name = 'blog'

urlpatterns = [
    path("", ArticleList.as_view(), name="list"),
    path("<int:pk>", ArticleDetail.as_view(), name="detail"),
    path("users", UserView.as_view(), name="user"),
    
]





