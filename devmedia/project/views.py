from django.shortcuts import render, HttpResponse
from .models import Pessoa

# Create your views here.
def index(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoas': pessoa})