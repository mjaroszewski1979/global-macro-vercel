# Python imports
import importlib

# Django imports
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from braces.views import GroupRequiredMixin

# App imports
from .models import Strategy, Market
from .forms import StrategyForm, SignUpForm
from . import utilities



class HomeView(View):
    
    def get(self, request):
        context = {}
        context['strategies'] = Strategy.objects.all()
        importlib.reload(utilities)
        context['zips'] = utilities.zips
        return render(request, 'index.html', context)

class StrategiesList(ListView):
    model = Strategy
    template_name = 'strategies_list.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = "New user was created successfully"

class StrategiesCreate(SuccessMessageMixin, CreateView):
    model = Strategy
    template_name = 'strategies_create.html'
    form_class = StrategyForm
    success_url = '.'
    success_message = "Strategy was created successfully"

class StrategiesUpdate(SuccessMessageMixin, UpdateView):
    model = Strategy
    template_name = 'strategies_update.html'
    form_class = StrategyForm
    success_url = '.'
    success_message = "Strategy was updated successfully"

class StrategiesDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    group_required = u"quant"
    template_name = 'strategies_delete.html'
    success_message = "Strategy was deleted successfully"
    
    def get_object(self):
        self.slug = self.kwargs.get('slug')
        return get_object_or_404(Strategy, slug=self.slug)

    def get_success_url(self):
        return reverse('strategies_list')

class StrategiesDetail(DetailView):
    template_name = 'strategies_detail.html'
    
    def get_object(self):
        queryset = Strategy.objects.all()
        self.slug = self.kwargs.get('slug')
        self.strats = Strategy.objects.filter(market__title__startswith=self.slug)
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['strats'] = self.strats
        context['slug'] = self.slug.upper()
        return context

class StrategyView(DetailView):
    template_name = 'strategy.html'
    
    def get_object(self):
        queryset = Strategy.objects.all()
        self.slug = self.kwargs.get('slug')
        self.strategy = get_object_or_404(Strategy, slug=self.slug)
        self.markets = self.strategy.market.all()
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['strategy'] = self.strategy
        context['markets'] = self.markets
        return context

class MarketDetail(DetailView):
    template_name = 'market_detail.html'
    
    def get_object(self):
        queryset = Market.objects.all()
        self.slug = self.kwargs.get('slug')
        self.market = get_object_or_404(Market, slug=self.slug)
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['market'] = self.market
        return context

class SearchView(View):
    template_name = 'search.html'

    def get(self, request):
        context = {}
        query = request.GET.get('query', '')
        strategies = Strategy.objects.filter(Q(title__icontains=query) |  Q(description__icontains=query))
        markets = Market.objects.filter(title__icontains=query)
        context['query'] = query
        context['strategy'] = strategies.first()
        context['market'] = markets.first()
        return render(request, 'search.html', context)


def page_not_found(response, exception):
    return render(response, '404.html')

def server_error(response):
    return render(response, '500.html')




    





