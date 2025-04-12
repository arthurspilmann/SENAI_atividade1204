from django.db import models
from django.core.exceptions import ValidationError
import re

def validar_nome_sem_numeros(value):
    if re.search(r'\d', value):
        raise ValidationError("O nome não pode conter números.")
    return value

class Colaborador(models.Model):
    nome = models.CharField(max_length=100, unique=True, validators=[validar_nome_sem_numeros])
    cpf = models.CharField(max_length=14)
    setor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class EPI(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    validade = models.DateField()

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    epi = models.ForeignKey(EPI, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()

    def __str__(self):
        return f"{self.colaborador} - {self.epi}"
    
def validar_nome_sem_numeros(value):
    if re.search(r'\d', value):
        raise ValidationError('O nome não pode conter números.')

