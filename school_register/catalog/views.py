from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import Mark
from .models import Student
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentListView(generic.ListView):
    model = Student
    template_name = 'student_list.html'


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'student_detail.html'


class StudentCreate(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'


class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student')
    template_name = 'student_confirm_delete.html'



