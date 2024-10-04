from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

    def validate_ano(self, value):
        import datetime
        ano_atual = datetime.datetime.now().year

        # Verifica se o valor é um ano válido
        if value.year < 1888 or value.year > ano_atual:
            raise serializers.ValidationError("Ano do filme deve estar entre 1888 e o ano atual.")
        return value

