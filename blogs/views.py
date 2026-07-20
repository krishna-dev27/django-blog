from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog,Category

# Create your views here.
def posts_by_category(request,category_id):
    #PO = Category.objects.filter(id=category_id)
    #posts = Blog.objects.filter(category_id = category_id,status='Published')
    posts = Blog.objects.filter(category = category_id,status='Published')
    context = {
        'posts':posts
    }
    return render(request, 'posts_by_category.html',context)
    