from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def root(request):
    return HttpResponseRedirect("home")

def home(request):
    response = render(request, "index.html")
    return HttpResponse(response)

