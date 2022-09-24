from django import forms
from .models import UserOrder, Account


class EmailtoBuyForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = ['account_id']

        widgets = {
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


class CreateAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['title_image', 'image_1', 'image_2', 'title', 'level', 'full_acces', 'vbucks', 'bling_amount',
                  'gliders_amount', 'save_world', 'hot_og', 'platform', 'mail', 'outfits', 'emotions', 'description',
                  'acc_raiting', 'acc_price']
