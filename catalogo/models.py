from django.db import models

# Create your models here.


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    ano = models.DateField()  
    genero = models.CharField(max_length=50)
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo

