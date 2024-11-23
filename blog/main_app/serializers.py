from rest_framework import serializers
from .models import Article, LikeForArticle


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
