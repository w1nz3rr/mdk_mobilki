from django.contrib import admin
from django.urls import path, include, re_path
from main_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/articles/', ArticleAPIList.as_view()),
    path('api/articles/<int:pk>', ArticleAPIUpdate.as_view()),
    path('api/articlesdelete/<int:pk>', ArticleDestroyAPIView.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/articles/<int:article_id>/like/', LikeArticleView.as_view()),
    path('api/articles/<int:article_id>/unlike/', UnlikeArticleView.as_view()),
]