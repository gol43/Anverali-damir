from django import forms
from .models import Customer
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['bio', 'exp']

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'role')
        labels = {
            'username': 'Имя пользователя',
            'role': 'Роль',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].required = False
