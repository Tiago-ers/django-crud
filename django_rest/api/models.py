from secrets import choice
from django.db import models

# Create your models here.

class Tecnologia(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    TIPO_CONTRATACAO = [("CLT", "Empregado registrado pela CLT"), ("PJ", "Pessoa jurídica")]
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=50, null=False, blank=False)
    salario = models.FloatField(null=True, blank=False)
    local = models.CharField(max_length=50, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    contato = models.EmailField(null=True, blank=False)
    tipo_contrato = models.CharField(max_length=3, null=False, blank=False, choices=TIPO_CONTRATACAO)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.title
