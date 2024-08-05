from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser 

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label='Full Name')
    address = forms.CharField(widget=forms.Textarea, required=False, label='Address')
    contact = forms.CharField(max_length=15, required=False, label='Contact')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, label='Role')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'address', 'contact', 'password1', 'password2', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        user.address = self.cleaned_data['address']
        user.contact = self.cleaned_data['contact']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}), label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
