from django.urls import path, include


from .views import ArticleList, ArticleDetail, ArticleUpdate, ArticleDelete,UserList, UserDetail

app_name = 'api'


urlpatterns = [
    path('', ArticleList.as_view(), name='list'),
    path('<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('<int:pk>/update', ArticleUpdate.as_view(), name='update'),
    path('<int:pk>/delete', ArticleDelete.as_view(), name='delete'),





    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),

]






