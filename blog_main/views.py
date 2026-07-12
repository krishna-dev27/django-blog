from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import *

def home(request):
    categories = Category.objects.all()
    d={
        'categories':categories
    }
    return render(request,'home.html',d)