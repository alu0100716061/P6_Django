# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home (request):
	return render(request,"home.html")

def help (request):
        return HttpResponse("This is help!")

def about (request):
        return HttpResponse("This is about!")

