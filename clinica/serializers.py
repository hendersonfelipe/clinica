from rest_framework import serializers
from django.contrib.auth.models import User
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

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=['nome','cpf','email','sexo','telefone']

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consulta
        fields=['cliente','agenda']

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user