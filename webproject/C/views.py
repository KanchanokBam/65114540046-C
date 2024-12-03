from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.
class CourseListView(ListView):
    model = Coures
    
    context_object_name