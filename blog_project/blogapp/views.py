from django.shortcuts import render
from .models import post

def home(request):
    context = {
        'posts':post.objects.all()
    }
    return render(request, 'blogapp/home.html', context)
