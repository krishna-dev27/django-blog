from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import *
from extras.models import About
def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True, status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status = 'Published')
    #about us section 
    try:
        about = About.objects.get()
    except:
        about = None
    d={
   
        'featured_posts':featured_posts,
        'posts':posts,
        'about': about,

    }
    
    
    return render(request,'home.html',d)


