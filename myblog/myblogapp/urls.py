
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fullBlog/<str:blog_id>', views.fullBlog, name='fullBlog')
]