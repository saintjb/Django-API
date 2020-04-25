from django.shortcuts import render
from api.models import Movie, Rating
from rest_framework import viewsets
from api.serializers import MovieSerializer, RatingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
