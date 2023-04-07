from django.contrib import admin

# Register your models here.


from .models import BlogPosts

admin.site.register(BlogPosts)