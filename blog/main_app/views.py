from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


from .models import Article
from .serializers import ArticleSerializer
from .permissions_for_articles import *



class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrOnlyRead, )

class ArticleDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
