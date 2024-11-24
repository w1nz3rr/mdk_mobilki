from django.forms import model_to_dict
from rest_framework import generics, viewsets, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView


from .models import Article, LikeForArticle, User
from .serializers import ArticleSerializer, LikeForArticleSerializer, UserSerializer
from .permissions_for_articles import *
from .permissions_for_users import *


class UserAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserApiUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsCurrentUserOrOnlyRead, )


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


class LikeArticleView(generics.CreateAPIView):
    serializer_class = LikeForArticleSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        article_id = self.kwargs.get('article_id')
        article = generics.get_object_or_404(Article, id=article_id)

        if LikeForArticle.objects.filter(user_id=request.user.id, article_id=article.id).exists():
            return Response({'detail': 'You already liked this article.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={'user': request.user.id, 'article': article.id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnlikeArticleView(generics.DestroyAPIView):
    queryset = LikeForArticle.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        article_id = self.kwargs.get('article_id')
        return generics.get_object_or_404(LikeForArticle, user=self.request.user, article_id=article_id)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

