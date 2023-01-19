from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views
from clinica.views import *



router = routers.DefaultRouter()
router.register('Especialidades/', EspecialidadeViewSet)
router.register('Medico/', MedicoViewSet)
router.register('Agenda/', AgendaViewSet)
router.register('Cliente/', ClienteViewSet)
router.register('Consulta/', ConsultaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('', include(router.urls)),
]
