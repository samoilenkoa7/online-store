from django import forms
from .models import UserOrder


class EmailtoBuyForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = ['name', 'email', 'account_id']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Your name',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Your email',
            }),
            'account_id': forms.TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Account id',
            }),
        }
