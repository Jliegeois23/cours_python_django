from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse("Racine du lycée")

def detail(request,cursus_id):
  resp = 'result for cursus {}'.format(cursus_id)
  return HttpResponse(resp)