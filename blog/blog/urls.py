from django.contrib import admin
from django.urls import path, include
from main_app.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/articles/', ArticleAPIList.as_view()),
    path('api/articles/<int:pk>', ArticleAPIUpdate.as_view()),
    path('api/articlesdelete/<int:pk>', ArticleDestroyAPIView.as_view())
]