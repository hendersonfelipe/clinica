from django.db import models
#from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AbstractUser

class Especialidades(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidades,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Agenda(models.Model):
    data=models.DateField()
    medico=models.ForeignKey(Medico, blank=True,on_delete=models.CASCADE)
    horario=(("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),)
    hora = models.CharField(max_length=10, choices=horario)
    def __str__(self):
        return str(self.data)+' - '+self.medico.nome+ ' - '+self.hora

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    genero = (("1", "Prefiro não dizer"),
        ("2", "Masculino"),
        ("3", "Feminino"))
    sexo = models.CharField(max_length=20, choices=genero)
    telefone = models.CharField(max_length=11)
    def __str__(self):
        return self.nome

class Consulta(models.Model):
    cliente = models.ForeignKey(Cliente, blank=True, on_delete=models.CASCADE)
    agenda = models.ForeignKey(Agenda, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.cliente)+self.agenda