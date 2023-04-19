from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings

from .utilities import get_data, subscribe
from .models import Bitcoin


def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subscribe(email)                  
        messages.success(request, "Thank you for your email. ") 
        return redirect('success')
    get_data()
    bitcoin = get_object_or_404(Bitcoin, title='btc-usd')
    return render(request, 'index.html', {'bitcoin': bitcoin})

def success(request):
    return render(request, 'success.html')

def page_not_found(response, exception):
    return render(response, '404.html')

def server_error(response):
    return render(response, '500.html')






