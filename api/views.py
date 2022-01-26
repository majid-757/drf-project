from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View

from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerialiser, UserSerialiser



class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser



class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)






class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsSuperUserOrStaffReadOnly,)



# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response({"message":"revoked!"})



class TemplateView1(TemplateResponseMixin, ContextMixin, View):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        # template_name = 'reset.html'
        # return self.render_to_response(context)

        return render(request, 'reset.html', context)

