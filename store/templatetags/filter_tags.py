from django import template
from math import floor

register = template.Library()

@register.simple_tag
def selected_attr(request_slug , slug):
    if request_slug == slug: 
        return "selected"
    else: 
        return ''
