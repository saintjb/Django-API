from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import MovieViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]