from django.shortcuts import render
from django.template import loader

def index(request):
    context = {
        
    }
    return render(request, 'homepage/reghpage.html', context)
