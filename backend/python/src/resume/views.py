from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def index(request):
    return render(request, 'resume/index.html')

def profile(request):
    context = Profile.objects.all()
    return HttpResponse(context)

def details(request, profile_name):
    context = {'detail': Profile.objects.filter(path=profile_name).first()}
    return render(request, 'resume/details.html', context)