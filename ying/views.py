from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Happy Mothers Day, Ying!  - from Feng and Eric")