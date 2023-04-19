# Django imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# App imports
from .models import Strategy
 
 
class StrategyForm(forms.ModelForm):
 
    class Meta:

        model = Strategy
        fields = [
            "title",
            'slug',
            "market",
            'cagr',
            'sharpe',
            'long_only',
            'description']

class SignUpForm(UserCreationForm):

    class Meta:
        
        model = User
        fields = [
            'username', 
            'password1', 
            'password2', 
            ]