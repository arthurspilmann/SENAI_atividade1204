from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('colaboradores/', views.colaboradores_view, name='colaboradores'),
    path('epis/', views.epis_view, name='epis'),
    path('emprestimos/', views.emprestimos_view, name='emprestimos'),
    path('colaboradores/<int:colaborador_id>/', views.colaboradores_view, name='editar_colaborador'),
    path('colaboradores/excluir/<int:colaborador_id>/', views.excluir_colaborador_view, name='excluir_colaborador'),
    path('epis/editar/<int:epi_id>/', views.editar_epi_view, name='editar_epi'),
    path('epis/excluir/<int:epi_id>/', views.excluir_epi_view, name='excluir_epi'),
    path('home/', views.home_view, name='home'),
    path('relatorio/', views.relatorio_view, name='relatorio'),


]
