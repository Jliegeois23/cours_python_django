"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lycee import views
from lycee.views import StudentCreateView, StudentUpdateView, CursusCallView, ParticularCallView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lycee',views.index,name="index"),
    path('',views.index,name="index2"),
    path('lycee/<int:cursus_id>',views.detail,name='detail'),
    path('lycee/student/<int:student_id>',views.detail_student,name="detail_student"),
    path('lycee/cursuscall/view',views.callview,name="call view"),
    path('lycee/cursuscall/view/<int:presence_id>',views.detail_callview,name='update student'),
    path('lycee/student/create',StudentCreateView.as_view(),name='create student'),
    path('lycee/student/edit/<pk>',StudentUpdateView.as_view(),name='update student'),
    path('lycee/cursuscall/<cursus>',CursusCallView.as_view(),name='Call of row'),
    path('lycee/cursuscall',ParticularCallView.as_view(),name='Particular call of row'),
    
    
]