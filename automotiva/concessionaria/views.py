from django.shortcuts import render, get_object_or_404
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *

# Create your views here.
def listar_veiculo(request, categoria):
    query = request.GET.get('busca', '')
    page = request.GET.get('page', '')
    ordenar = request.GET.get('ordenar', '')
    if query:
        if categoria != "todos":
            veiculos = Veiculo.objects.filter(modelo__icontains=query, tipo=categoria)
        else:
            veiculos = Veiculo.objects.filter(modelo__icontains=query)
    else:
        try:
            if categoria != "todos":
                if ordenar:
                    veiculos = Veiculo.objects.all().filter(tipo=categoria).order_by(ordenar)
                else:
                    veiculos = Veiculo.objects.filter(tipo=categoria)
            else:
                if ordenar:
                    veiculos = Veiculo.objects.all().order_by(ordenar)
                else:
                    veiculos = Veiculo.objects.all()
            veiculos = Paginator(veiculos, 2)
            veiculos = veiculos.page(page)
        except PageNotAnInteger:
            veiculos = veiculos.page(1)
        except EmptyPage:
            veiculos = paginator.page(paginator.num_pages)

    return render(request, "veiculo_list.html", {'veiculos': veiculos})

def perfil_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo,id=id)
    return render(request, "veiculo.html", {'veiculo': veiculo})