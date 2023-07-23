from django.contrib.auth import get_user_model
from django import forms
from . import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ("picture",)


class SignupForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("This email is already in use. Please use a different email."))
        return email

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError(_("Password must match."))
        return password_confirm
