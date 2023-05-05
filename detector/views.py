# Django imports
from django.shortcuts import render

# App imports
from .utilities import get_result, get_score


def index(request):
    '''
    This function handles requests to the index page
    :type name: HttpRequest object
    :param request: contains metadata about the request

    '''
    # Render the index.html template
    return render(request, 'index.html')


def ai_detector(request):
    '''
    This function handles requests to the AI detector page
    :type name: HttpRequest object
    :param request: contains metadata about the request

    '''
    # Get the content from the POST request
    content = request.POST.get('content')
    # Use a separate function to get the result from the content
    result = get_result(content)
    # Use a separate function to get the score from the result
    score = get_score(result)
    # Create a dictionary with the score to pass to the template
    if score == 'error':
        return render(request, 'error.html')
    else:
        context = {'score' : score}
        # Render the result.html template with the score context
        return render(request, 'result.html', context)
    
def page_not_found(response, exception):
    """
    This function is called whenever a page is not found (404 error) in the web application. It takes two arguments:
    - response: The HTTP response object.
    - exception: The exception that caused the 404 error.

    The function renders the '404.html' template and returns the response with the rendered template. This template is 
    typically a custom error page that is displayed to the user when a page is not found.

    """
    # Render the 404.html template
    return render(response, '404.html')

def server_error(response):
    """
    This function is called whenever there is a server error (500 error) in the web application. It takes one argument:
    - response: The HTTP response object.

    The function renders the '500.html' template and returns the response with the rendered template. This template is 
    typically a custom error page that is displayed to the user when there is a server error. 

    """
    # Render the 500.html template
    return render(response, '500.html')



