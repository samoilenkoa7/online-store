from django import forms
from .models import UserOrder, Account


class EmailtoBuyForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = ['name', 'email', 'account_id']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email',
            }),
            'account_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Account id',
            }),
        }


class SortForm(forms.Form):

    choices = (
        ('-acc_price', 'High to low'),
        ('acc_price', 'Low to high'),
    )
    sort_form = forms.TypedChoiceField(choices=choices, widget=forms.Select(attrs={
        'class': 'form-control',
        }))