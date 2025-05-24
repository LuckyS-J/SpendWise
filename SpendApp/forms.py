from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

  def clean_email(self):
      email = self.cleaned_data.get('email')
      if User.objects.filter(email=email).exists():
          raise forms.ValidationError("This email address is already registered.")
      return email
  
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )