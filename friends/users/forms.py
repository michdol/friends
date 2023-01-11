from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class CreateUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            User.USERNAME_FIELD,
            User.get_email_field_name(),
            'password1',
            'password2'
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=8,
        max_length=150
    )
    password = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput()
    )

    class Meta:
        fields = ('username', 'password')
