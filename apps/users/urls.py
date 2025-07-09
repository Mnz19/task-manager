from django.urls import path
from rest_framework import routers
from django.urls import include
from apps.users.views.user import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
