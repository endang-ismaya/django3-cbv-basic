# from django.shortcuts import render
from django.urls import reverse_lazy
from cbv.models import School, Student
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('cbv:list')


class SchoolUpdateView(UpdateView):
    model = School
    fields = ['name', 'principal']
    template_name = 'cbv/cbv_school_create.html'


class SchoolCreateView(CreateView):
    model = School
    fields = ['name', 'principal', 'location']
    template_name = 'cbv/cbv_school_create.html'


class StudentListView(ListView):
    context_object_name = 'students'
    template_name = 'cbv/cbv_student_list.html'
    model = Student


class SchoolListView(ListView):
    context_object_name = 'schools'
    template_name = 'cbv/cbv_school_list.html'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'cbv/cbv_school_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(TemplateView):
    template_name = 'cbv/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'This is a secret'
        return context
