from django.shortcuts import render

from .models import BlogPosts

# Create your views here.

def index (request):
     blogs = BlogPosts.objects.all()
     context={
          'blogs':blogs
     }

     return  render(request, 'index.html', context)

def fullBlog (request, blog_id):
     blogs = BlogPosts.objects.filter(id = blog_id)
     return render (request, 'fullBlog.html', {'blogs':blogs})