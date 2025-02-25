from numbers import Number

from django.shortcuts import render
from .models import Student, Faculty, Group, Specialty, Department, Teacher
from django.views.generic import DetailView



def home_page(request):
    return render(request,'students/home_page.html')

def facultys(request):
    data = Faculty.objects.order_by('Title')
    return render(request, 'students/facultys.html', {'data': data})

def schedule(request):
    data = Group.objects.order_by('Number')
    return render(request, 'students/schedule.html', {'data': data})

class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'students/details_view.html'
    context_object_name = 'faculty'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'students/details_schedule.html'
    context_object_name = 'group'