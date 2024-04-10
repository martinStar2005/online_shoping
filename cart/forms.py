from django import forms

class AddToCartForm(forms.Form):
    """Create Cart Form"""

    CHOISES_NUMBER = ((i, str(i)) for i in range(20))

    number = forms.TypedChoiceField(choices=CHOISES_NUMBER, coerce=int)