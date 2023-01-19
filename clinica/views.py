from rest_framework import viewsets
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import *
from .models import *
from datetime import date
import datetime
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class EspecialidadeViewSet(viewsets.ModelViewSet):
    serializer_class=EspecialidadeSerializer
    queryset=Especialidades.objects.all()

class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class= MedicoSerializer
    queryset=Medico.objects.all()

class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class= AgendaSerializer
    queryset=Agenda.objects.all()

    def create(self, request):
        data_c=request.POST.get('data')
        medicoForm=request.POST.get('medico')
        horaForm=request.POST.get('hora')
        h=date.today()
        td=str(h)
        diaForm=datetime.datetime.fromisoformat(data_c)
        hoje=datetime.datetime.fromisoformat(td)
        query=Agenda.objects.filter(data=diaForm).filter(medico=medicoForm).filter(hora=horaForm)
        print(horaForm)
        con=Medico.objects.get(id=int(medicoForm))

        if(hoje<diaForm):
            if(len(query)<=0):
                con=Medico.objects.get(id=int(medicoForm))
                
                ag=Agenda(data=diaForm,medico=Medico.objects.get(id=con.id), hora=horaForm)
                ag.save()
            elif(len(query)>0):
                return Response('Este médico já está cadastrado para essa data e horário.')
            else:
                return Response('Erro Inesperado!')
        elif(hoje>diaForm):
            return Response('A data selecionada é anterior a atual.')
        else:
            return Response('Erro inesperado!')
        return Response('Agenda para o médico '+con.nome+' Cadastrado com sucesso!')

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class= ClienteSerializer
    queryset=Cliente.objects.all()

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class= ConsultaSerializer
    queryset=Consulta.objects.all()

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)