from django.contrib import admin
from django.urls import path, include
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users', UserAPIList.as_view()),
    path('api/users/<int:pk>', UserAPIView.as_view()),
]