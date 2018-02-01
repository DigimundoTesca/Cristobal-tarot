from django.shortcuts import render

def index(request):
    template = 'index.html'
    context = {
        'title': "Cristobal - Tarot",
    }
    return render(request, template, context)
