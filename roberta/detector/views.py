from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def detector(request):
    pass
