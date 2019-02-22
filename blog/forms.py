from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model  = User
        fields = ('username', 'first_name', 'last_name', 'email','birth_date','password1', 'password2')

class Comment(forms.Form):
    blog_id = forms.CharField(widget=forms.HiddenInput())
    name    = forms.CharField(label="Your Name", max_length=255)
    email   = forms.CharField(label="Email",max_length=255)
    comment = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
