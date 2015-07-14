from shoppy.models import Movies, Genres
from rest_framework import viewsets
from shoppy.serializers import MoviesSerializer, GenresSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class GenresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer