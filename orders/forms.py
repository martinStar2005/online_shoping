from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'mobile_number', 'address', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'If you want, You can write your note here!'}),
            'address': forms.Textarea(attrs={'rows':3})
        }