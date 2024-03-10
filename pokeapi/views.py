from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
import requests
from .forms import IniciarSessaoForm, RegistroUsuarioForm


POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon/'

#Página principal exibindo os pokemons 

def pagina_principal(request):
    limit = 50
    offset = int(request.GET.get('offset', 0))
    url = f'{POKEAPI_URL}?limit={50}&offset={offset}'

    resposta = requests.get(url)
   
    if resposta.status_code == 200:
        informacao = resposta.json()
        resultados = informacao.get('results', [])
        contexto = {
            'resultados': resultados,
            'proxima_pagina': offset + limit,
            'pagina_anterior': max(offset - limit, 0),
        }
        return render(request, 'index.html', contexto)
    else:
        mensagem_erro = "Não foi possível carregar os Pokémons."
        contexto = {
            'mensagem_erro': mensagem_erro,
        }
        return render(request, 'index.html', contexto)


#Visualizar Pokemon
@login_required  
def visualizar_pokemon(request, pokemon_name):
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
    if resposta.status_code == 200:
        info_pokemon = resposta.json()
        contexto = {
            'pokemon': info_pokemon, 
        }
        return render(request, 'visualizar_pokemon.html', contexto)
    else:
        mensagem_erro = f"Mão foi possivel encontrar a informação do pokemon: {pokemon_name}."
        contexto = {
            'mensagem_erro': mensagem_erro,
        }
        return render(request, 'visualizar_pokemon.html', contexto)

#Registro de usuario
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuer = form.save()
            return redirect('iniciar_sessao')
    else:
        form = RegistroUsuarioForm()
    contexto = {'form': form}
    return render(request, 'registration/registrar.html', contexto)


def iniciar_sessao(request):
    if request.method == 'POST':
        form = IniciarSessaoForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pagina_principal')
    else:
        form = IniciarSessaoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'registration/login.html', contexto)
 
def encerrar_sessao(request):
    logout(request)
    return redirect('pagina_principal')

