from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    telefone = models.IntegerField()
    cidade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome