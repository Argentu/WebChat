from chat.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                       'placeholder': 'Enter username...'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Enter password...'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Confirm password...'}))

    class Meta:
        model = MyUser
        fields = ('username', 'password1')
