from rest_framework import viewsets
from .serializers import *
from .models import *
from datetime import date
import datetime
from rest_framework.response import Response
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
