from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse

from .models import Cursus
from .models import Student
from django.views.generic.edit import CreateView
from lycee.templates.lycee.forms import StudentForm


def detail(request,cursus_id):
    resp = 'result for cursus {}'.format(cursus_id)
    return HttpResponse(resp)

def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)

    context = {'liste' : result_list}

    return render(request, 'lycee/student/detail_student.html', context)

def index(request):
    result_list = Cursus.objects.order_by('name')

    context = {
        'liste' : result_list,
    }
    return  render(request, 'lycee/index.html', context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse('detail_student', args=(self.object.pk,))