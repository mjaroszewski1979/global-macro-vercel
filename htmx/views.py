from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# App imports
from .forms import RegisterForm
from .models import UserCars


class HomeView(View):

    """HomeView Class will render index page."""
    
    def get(self, request):
        """
        This function is responsible for handling HTTP GET requests.

        :type name: HttpRequest object
        :param request: contains metadata about the request
        """
        return render(request, 'index.html')

class RegisterView(FormView):

    """
    RegisterView Class will render register page. It uses RegisterForm and it will
    redirect to the login page after successful registration.

    """
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Login(LoginView):

    """LoginView Class will render login page."""

    template_name = 'login.html'

class CarList(LoginRequiredMixin, ListView):

    """
    CarListView Class will render cars page. In case of request
    being made via HTMX it will inject car_list_element partial.
    It uses UserCars model and sets context object name to 'cars'.
    This class will work with LoginRequiredMixin to secure view 
    by forcing the client to authenticate with a valid logged-in User.
    It also takes advantage of QuerySet prefetch_related method
    to avoid additional queries when accessing the related objects.
    """

    template_name = 'cars.html'
    model = UserCars
    context_object_name = 'cars'

    def get_template_names(self):
        if self.request.htmx:
            return 'partials/car_list_elements.html'
        return 'cars.html'
        
    def get_queryset(self):
        return UserCars.objects.prefetch_related('car').filter(user=self.request.user)


