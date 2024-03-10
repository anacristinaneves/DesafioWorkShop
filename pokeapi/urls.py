from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    #Página principal, Visualizar Pokemon, Cadastrar-se, Iniciar sessão e encerrar sessão.

    path('', views.pagina_principal, name='pagina_principal'),
    path('pokemon/<str:pokemon_name>/', views.visualizar_pokemon, name='visualizar_pokemon'),
    path('registro/', views.registro_usuario, name='cadastrar_usuario'),
    path('iniciar-sessao/', views.iniciar_sessao, name='iniciar_sessao'),
    path('encerrar-sessao/', views.encerrar_sessao, name='encerrar_sessao'),
]
