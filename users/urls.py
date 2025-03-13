from django.urls import path, include
from users.views import UserViewSet, RegisterViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('register', RegisterViewSet, basename='register')


urlpatterns = [
    path("", include(router.urls))
]
