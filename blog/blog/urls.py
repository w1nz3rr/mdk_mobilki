from django.contrib import admin
from django.urls import path, include
from main_app.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
    # path('api/users', UserViewSet.as_view({'get': 'list'})),
    # path('api/users/<int:pk>', UserViewSet.as_view({'put': 'update'})),
    # path('api/usersdetail/<int:pk>', UserDetailAPIView.as_view()),
]