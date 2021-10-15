from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    context = Profile.objects.all()
    return HttpResponse(context)