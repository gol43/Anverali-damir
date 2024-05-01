from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", strip=False, widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role')
        help_texts = {'username': None}
        labels = {
            'username': 'Имя пользователя',
            'role': 'Роль',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
