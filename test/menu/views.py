from django.shortcuts import render
from .models import Menu, SubMenu


def main(request):
    points = Menu.objects.filter(page='main')
    return render(request, 'menu.html', {'points': points})


def page(request, name):
    last_points = Menu.objects.filter(page=Menu.objects.get(slug=name).page)
    points = SubMenu.objects.values(
        'main_menu__name', 'submenu__name', 'submenu__slug'
    ).filter(
        main_menu=Menu.objects.get(slug=name).id
    )
    return render(request, 'page.html',
                  {'points': points, 'last_points': last_points})
