from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')


