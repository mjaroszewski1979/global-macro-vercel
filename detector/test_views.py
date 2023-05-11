# Django imports
from django.test import TestCase, Client
from django.urls import reverse, resolve

# App imports
from .views import index, ai_detector


# Testing detector app
class DetectorTest(TestCase):
    '''
    This is a unit test class for testing the views of the "ai_detector" app.

    '''

    
    def setUp(self):
        '''
        This method is a special method in the test case class and is executed before each test method in the class. It sets up a new client instance.

        '''
        self.client = Client()

    
    def test_index_url_is_resolved(self):
        '''
        This method tests whether the URL "index" is resolved correctly and whether it maps to the "index" view function.

        '''
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    
    def test_index_get(self):
        '''
        This method tests whether the "index" view function returns a valid HTTP response with a status code of 200, and whether the response contains the expected content and uses the correct template.

        '''
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'AI Detector | Home', status_code=200)
        self.assertTemplateUsed(response, 'index.html')

    
    def test_ai_detector_url_is_resolved(self):
        '''
        This method tests whether the URL "ai_detector" is resolved correctly and whether it maps to the "ai_detector" view function.

        '''
        url = reverse('ai_detector')
        self.assertEquals(resolve(url).func, ai_detector)

    
    def test_ai_detector_get(self):
        '''
        This method tests whether the "ai_detector" view function returns a valid HTTP response with a status code of 200, and whether the response contains the expected content and uses the correct template.

        '''
        response = self.client.get(reverse('ai_detector'))
        self.assertContains(response, 'AI Detector | Result', status_code=200)
        self.assertTemplateUsed(response, 'result.html')

    
    def test_ai_detector_post(self):
        '''
        This method tests whether the "ai_detector" view function can correctly handle a POST request with the given data. It sends a POST request to the "ai_detector" URL with the given data and verifies that the response contains the expected content and the "Back to AI Detector>>>" link.

        '''
        data={
            'content' : 'I like you. I love you.'
        }
        response = self.client.post(reverse('ai_detector'), data, follow=True)
        self.assertContains(response, 'AI Detector | Result', status_code=200)
        self.assertTrue(b'Back to AI Detector>>>' in response.content)

    
    def test_handler404(self):
        '''
        This method tests whether the custom 404 error page is displayed when an invalid URL is accessed. It sends a GET request to an invalid URL and verifies that the response contains the expected content and uses the correct template.

        '''
        response = self.client.get('/some_url/')
        self.assertContains(response, 'AI Detector | Page not found', status_code=404)
        self.assertTemplateUsed(response, '404.html')
