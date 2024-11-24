from rest_framework import serializers
from .models import Article, LikeForArticle, User


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    like_count = serializers.IntegerField(source='likeforarticle_set.count', read_only=True)  # Подсчет лайков
    class Meta:
        model = Article
        fields = '__all__'


class LikeForArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeForArticle
        fields = ['user', 'article']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'is_active', 'date_joined']
