from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'name', 'username', 'password', 'date_of_birth')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'name', 'username', 'date_of_birth')

    def clean_password2(self):
        if self.cleaned_data.get('password1') and self.cleaned_data.get('password2') and \
                self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            raise forms.ValidationError("Passwords don't match!")
        return self.cleaned_data.get('password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'name', 'username', 'date_of_birth', 'password', 'is_staff', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial['password']
