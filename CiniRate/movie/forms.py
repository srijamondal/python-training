from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review

class Registrationform(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']
        
        widgets = {
            'rating':forms.Select(attrs={'class': 'form-select'}),
            'comment':forms.Textarea(attrs={'class': 'form-control','rows':4}),
        }