from django import forms
from .models import *


class MyForm(forms.ModelForm):
    class Meta:
        model = ModelloPosti
        fields = ['posto1', 'posto2', 'posto3', 'posto4', 'posto5', 'posto6', 'posto7', 'posto8', 'posto9', 'posto10', 'posto11', 'posto12', 'posto13', 'posto14', 'posto15', 'posto16', 'posto17', 'posto18', 'posto19', 'posto20', 'posto21','posto22']
        
        # Customizing widgets to add class and placeholder
        widgets = {
            'posto1': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto2': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto3': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto4': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto5': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto6': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto7': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto8': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto9': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto10': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto11': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto12': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto13': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto14': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto15': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto16': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto17': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto18': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto19': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto20': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto21': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
            'posto22': forms.TextInput(attrs={'class': 'formBox', 'placeholder': 'Cognome'}),
        }




class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'inputBox',
            'placeholder': 'Nome Utente'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'inputBox',
            'placeholder': 'Password'
        }
    ))
