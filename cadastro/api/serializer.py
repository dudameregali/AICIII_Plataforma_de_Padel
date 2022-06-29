from dataclasses import Field, field, fields
from rest_framework import serializers
from cadastro.models import Cadastro

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id', 'nome', 'cpf', 'telefone', 'cidade']