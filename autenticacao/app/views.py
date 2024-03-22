from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def reguistrar_usuario(request):
    user = request.user
    
    if user.is_staff:

        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            tipo = request.POST['tipo_usuario']

            if tipo == "administrador":
                user = User.objects.create_user(username, email, password)
                user.is_staff = True
                user.save()
            else:
                user = User.objects.create_user(username, email, password)

            return redirect('listar_usuario')
    else:
        messages.error(request, 'Usuário não encontrado.')
        return redirect('Permissão negada.')
    
    return render(request, "registrar.html")

@login_required
def listar_usuario (request):
    usuarios = User.objects.all()

    return render(request, "listar.html", {'usuarios': usuarios})

@login_required
def remover_usuario(request, id):
    user = request.user
    if user.has_perm('user.delete_user'):
        try:
            usuario = User.objects.get(id = id)
            if request.method == "POST":
                usuario.delete()
                return redirect('listar_usuario')
        except:
            messages.error(request, 'Usuário não encontrado.')
            return redirect('/listar_usuario/')
    else:
        messages.error(request, 'Permissão negada.')
        return redirect('/listar_usuario/')

    return render(request, 'delete.html', {'usuario': usuario})

def logar(request):
    next = request.GET.get('next', '/listar_usuario/')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)

        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "login.html", {'redirect_to': next})

def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)