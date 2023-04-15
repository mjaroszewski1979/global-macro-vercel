from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    """
    This class will extend UserCreationForm to provide registration fields 
    for User model
    """
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]