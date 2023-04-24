from django.shortcuts import render
from .utilities import get_result, get_data

def index(request):
    return render(request, 'index.html')

def ai_detector(request):
    content = request.POST.get('content')
    result = get_result(content)
    data = get_data(result)
    context = {'data' : data}
    return render(request, 'result.html', context)



