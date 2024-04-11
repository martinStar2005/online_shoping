from django import forms

class AddToCartForm(forms.Form):
    """Create Cart Form"""

    CHOISES_QUANTITY = ((i, str(i)) for i in range(1, 20))

    quantity = forms.TypedChoiceField(choices=CHOISES_QUANTITY, coerce=int)