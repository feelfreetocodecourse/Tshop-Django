from django import template
from math import floor

register = template.Library()

@register.simple_tag
def get_order_status_class(status):
    if status == "COMPLETED": 
        return "success"
    elif status=="PENDING":
        return 'warning'
    else:
        return 'info'
