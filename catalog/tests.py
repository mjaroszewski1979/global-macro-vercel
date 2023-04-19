# Django imports
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group


# App imports
from . import views
from .models import Strategy


# Testing project app
class CatalogTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.new_strategy = Strategy.objects.create(
            title = 'momentum',
            slug = 'momentum',
            cagr = 7,
            sharpe = 1,
            long_only = False,
            description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, qui sed similique doloribus incidunt voluptatem debitis doloremque iure suscipit dignissimos!'
        )
        self.new_strategy.save()
        self.new_strategy.market.create(
            title = 'stocks',
            slug = 'stocks'
        )
        group_name = 'quant'
        self.group = Group(name=group_name)
        self.group.save()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def tearDown(self):
        self.user.delete()
        self.group.delete()

    # Index view tests
    def test_index_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, views.HomeView)

    def test_index_get(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Quant Catalog | Home', status_code=200)
        self.assertTemplateUsed(response, 'index.html')
        strategy = response.context['strategies'][0]
        self.assertEquals(str(strategy), str(self.new_strategy))

    # CAGR view tests
    def test_cagr_url_is_resolved(self):
        url = reverse('cagr')
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_cagr_get(self):
        response = self.client.get(reverse('cagr'))
        self.assertContains(response, 'Quant Catalog | CAGR', status_code=200)
        self.assertTemplateUsed(response, 'cagr.html')

    # Sharpe view tests
    def test_sharpe_url_is_resolved(self):
        url = reverse('sharpe')
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_sharpe_get(self):
        response = self.client.get(reverse('sharpe'))
        self.assertContains(response, 'Quant Catalog | Sharpe', status_code=200)
        self.assertTemplateUsed(response, 'sharpe.html')

    # Long view tests
    def test_long_url_is_resolved(self):
        url = reverse('long')
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_long_get(self):
        response = self.client.get(reverse('long'))
        self.assertContains(response, 'Quant Catalog | Long Only', status_code=200)
        self.assertTemplateUsed(response, 'long.html')

    # Serach view tests
    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, views.SearchView)

    def test_search_get(self):
        response = self.client.get(reverse('search'))
        self.assertContains(response, 'Quant Catalog | Search', status_code=200)
        self.assertTemplateUsed(response, 'search.html')

    def test_search_query(self):
        response = self.client.get('/search/?query=stocks')
        query = response.context['query']
        context_strategy = response.context['strategy']
        context_market = response.context['market']
        self.assertEquals(query, 'stocks')
        self.assertEquals(str(context_market), 'stocks')
        self.assertEquals(context_strategy, None)

    # Signup view tests
    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, views.SignUpView)

    def test_signup_get(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Quant Catalog | Signup', status_code=200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_post(self):
        data={
            'username' : 'maciej123',
            'password1' : 'jaroszewski',
            'password2' : 'jaroszewski'
        }
        response = self.client.post(reverse('signup'), data, follow=True)
        self.assertContains(response, 'Quant Catalog | Login', status_code=200)
        self.assertTemplateUsed(response, 'login.html')

    # Login view tests
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Quant Catalog | Login', status_code=200)
        self.assertTemplateUsed(response, 'login.html')

    # Logout view tests
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    # Strategies create view tests
    def test_strategies_create_url_is_resolved(self):
        url = reverse('strategies_create')
        self.assertEquals(resolve(url).func.view_class, views.StrategiesCreate)

    def test_strategies_create_get(self):
        response = self.client.get(reverse('strategies_create'))
        self.assertContains(response, 'Quant Catalog | Create Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_create.html')

    def test_strategies_create_post(self):
        data={
            'title' : 'trend_following',
            'slug' : 'trendfollowing',
            'cagr' : 5,
            'sharpe' : 1,
            'market' : 'stocks',
            'long_only' : True,
            'description' : 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
        }
        response = self.client.post(reverse('strategies_create'), data, follow=True)
        self.assertContains(response, 'Quant Catalog | Create Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_create.html')

    # Strategies update view tests
    def test_strategies_update_url_is_resolved(self):
        url = reverse('strategies_update', args= (self.new_strategy.slug, ))
        self.assertEquals(resolve(url).func.view_class, views.StrategiesUpdate)

    def test_strategies_update_get(self):
        response = self.client.get(reverse('strategies_update', args= (self.new_strategy.slug, )))
        self.assertContains(response, 'Quant Catalog | Update Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_update.html')

    def test_strategies_update_post(self):
        data={
            'title' : 'trend_following',
            'slug' : 'trendfollowing',
            'cagr' : 5,
            'sharpe' : 1,
            'market' : 'stocks',
            'long_only' : True,
            'description' : 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
        }
        response = self.client.post(reverse('strategies_update', args= (self.new_strategy.slug, )), data, follow=True)
        self.assertContains(response, 'Quant Catalog | Update Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_update.html')

    # Strategy detail view tests
    def test_strategy_detail_url_is_resolved(self):
        url = reverse('strategy_detail', args= (self.new_strategy.slug, ))
        self.assertEquals(resolve(url).func.view_class, views.StrategyView)

    def test_strategy_detail_get(self):
        response = self.client.get(reverse('strategy_detail', args= (self.new_strategy.slug, )))
        self.assertContains(response, 'Quant Catalog | ' + self.new_strategy.title.capitalize(), status_code=200)
        self.assertTemplateUsed(response, 'strategy.html')

    # Strategies delete view tests
    def test_strategies_delete_url_is_resolved(self):
        url = reverse('strategies_delete', args= (self.new_strategy.slug, ))
        self.assertEquals(resolve(url).func.view_class, views.StrategiesDelete)

    def test_strategies_delete_user_in_group(self):
        self.group.user_set.add(self.user)
        self.group.save()
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('strategies_delete', args= (self.new_strategy.slug, )), follow=True)
        self.assertContains(response, 'Quant Catalog | Delete Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_delete.html')

    def test_strategies_delete_user_not_in_group(self):
        response = self.client.get(reverse('strategies_delete', args= (self.new_strategy.slug, )), follow=True)
        self.assertTemplateUsed(response, 'login.html')

    def test_strategies_delete_post_user_in_group(self):
        self.group.user_set.add(self.user)
        self.group.save()
        self.client.login(username='testuser', password='12345')
        data= {
            'value' : 'Delete'
        }
        response = self.client.post(reverse('strategies_delete', args= (self.new_strategy.slug, )), data, follow=True)
        strategies_count = Strategy.objects.count()
        self.assertTemplateUsed(response, 'strategies_list.html')
        self.assertEquals(strategies_count, 0)


    



    





        
