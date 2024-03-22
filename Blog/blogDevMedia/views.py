from django.shortcuts import render, get_object_or_404

from .models import Postagem

# Create your views here.
def postagem(request):
    postagens = Postagem.objects.all()

    return render(request, 'home.html', {'postagens': postagens})

def postagem_list (request, id):
    post = get_object_or_404(Postagem, id=id)

    return render(request, "post.html", {"post": post})