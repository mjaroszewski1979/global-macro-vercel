
# Django imports
from django.test import TestCase, Client
from django.urls import reverse, resolve


# App imports
from .views import index, ai_detector


# Testing detector app
class DetectorTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'AI Detector | Home', status_code=200)
        self.assertTemplateUsed(response, 'index.html')

    def test_ai_detector_url_is_resolved(self):
        url = reverse('ai_detector')
        self.assertEquals(resolve(url).func, ai_detector)

    def test_ai_detector_get(self):
        response = self.client.get(reverse('ai_detector'))
        self.assertContains(response, 'AI Detector | Result', status_code=200)
        self.assertTemplateUsed(response, 'result.html')

    def test_ai_detector_post(self):
        data={
            'content' : 'I like you. I love you.'
        }
        response = self.client.post(reverse('ai_detector'), data, follow=True)
        self.assertContains(response, 'AI Detector | Result', status_code=200)
        self.assertTrue(b'Back to AI Detector>>>' in response.content)

    def test_handler404(self):
        response = self.client.get('/some_url/')
        self.assertContains(response, 'AI Detector | Page not found', status_code=404)
        self.assertTemplateUsed(response, '404.html')
