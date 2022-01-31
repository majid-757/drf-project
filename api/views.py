from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View

from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerialiser, UserSerialiser




class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()

    serializer_class = ArticleSerialiser

    filterset_fields = ['status', 'author__username']

    ordering_fields = ["publish", "status"]

    ordering = ["-publish"]

    search_fields = ["title", "content", "author__username", "author__first_name", "author__last_name"]




    def get_permissions(self):
    
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]






class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsSuperUserOrStaffReadOnly,)







class TemplateView1(TemplateResponseMixin, ContextMixin, View):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        # template_name = 'reset.html'
        # return self.render_to_response(context)

        return render(request, 'reset.html', context)

