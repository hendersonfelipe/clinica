from rest_framework import serializers
from .models import *
class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Especialidades
        fields=['nome',]

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medico
        fields=['nome','crm','email','telefone','especialidade']

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agenda
        fields=['data','medico','hora']