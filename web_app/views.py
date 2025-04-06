from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    return HttpResponse("This is the home page of the To-Do List web app.")

