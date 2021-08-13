from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app_3(request):
    return HttpResponse('this is from app2')