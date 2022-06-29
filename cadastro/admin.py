from django.contrib import admin
from cadastro.models import Cadastro

# Register your models here.
class Participantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'telefone', 'cidade')
    list_display_links = (('id', 'nome', 'cpf', 'telefone', 'cidade'))
    search_fields = ('nome',)

admin.site.register(Cadastro, Participantes)