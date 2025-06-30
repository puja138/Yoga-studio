# myapp/forms.py

from django import forms
from .models import Member

class JoinForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'password', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Create Password'}),
            'address': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your Address'}),
        }
