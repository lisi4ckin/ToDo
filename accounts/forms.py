from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget={forms.PasswordInput()})

    class Meta:
        model = Account
        fields = ('email', 'name', 'username', 'password', 'date_of_birth')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user


