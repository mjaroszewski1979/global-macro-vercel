from django.shortcuts import render
from .utilities import get_result, get_score

# This function handles requests to the index page
def index(request):
    # Render the index.html template
    return render(request, 'index.html')

# This function handles requests to the AI detector page
def ai_detector(request):
    # Get the content from the POST request
    content = request.POST.get('content')
    # Use a separate function to get the result from the content
    result = get_result(content)
    # Use a separate function to get the score from the result
    score = get_score(result)
    # Create a dictionary with the score to pass to the template
    context = {'score' : score}
    # Render the result.html template with the score context
    return render(request, 'result.html', context)



