from django.shortcuts import render, get_object_or_404
from .models import Question
from django.template import loader
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    #Modo ruim de renderizar
    """latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br> <br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)"""

    #Modo completo
    """latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))"""

    #Modo reduzido
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #Modo completo
    """try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist :´)")
    return render(request, 'polls/detail.html', {'question': question})"""

    #Modo reduzido
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)