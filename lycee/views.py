from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus
from django.template import loader
from .models import Student


# def index(request):
  # return HttpResponse("Racine du lycée")

def detail(request,cursus_id):
  resp = 'result for cursus {}'.format(cursus_id)
  return HttpResponse(resp)

def index (request):
  result_list = Cursus.objects.order_by('name')
  #chargement du template
  '''
  template = loader.get_template('lycee/index.html')
  '''
  #context
  context = {
    'liste' : result_list,
  }
  '''
  return HttpResponse(template.render(context, request))
  '''
  return render (request, 'lycee/index.html', context)

def detail_student(request,student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {'liste' : result_list}

  return render (request, 'lycee/student/detail_student.html', context)