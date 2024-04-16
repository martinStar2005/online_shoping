from django import template

register = template.Library()

@register.filter
def en_to_fa(value):
    value = str(value)
    trans_fa = value.maketrans('0123456789', '۰١٢٣٤٥٦٧٨٩')
    return value.translate(trans_fa)