from django import template

register = template.Library()


@register.filter
def comment_active(comment):
    return comment.filter(active=True)
