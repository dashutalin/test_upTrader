from django import template
from ..models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(name):
    return Menu.objects.filter(page=name)
