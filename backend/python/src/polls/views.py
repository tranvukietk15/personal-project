from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    
    return render(request, 'polls/main.html')

def questions(request):
    list_question = Question.objects.all()
    context = {'questions': list_question}
    return render(request, 'polls/questions.html', context);

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def cc(request):
    return HttpResponse("You're testing")