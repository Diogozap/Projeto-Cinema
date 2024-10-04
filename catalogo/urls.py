from django.urls import path
from .views import FilmeCriar, FilmeDetalhar
urlpatterns = [
    path('api/filmes/', FilmeCriar.as_view(), name='filme-criar'), 
    path('api/filmes/<int:pk>/', FilmeDetalhar.as_view(), name='filme-detalhes'),
]

