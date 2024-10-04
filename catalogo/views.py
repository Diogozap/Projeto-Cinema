from rest_framework import generics
from .models import Filme
from .serializers import FilmeSerializer
from rest_framework.filters import SearchFilter
from rest_framework import generics

class FilmeCriar(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['genero']

class FilmeDetalhar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

