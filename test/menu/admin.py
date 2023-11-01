from django.contrib import admin

from .models import Menu, SubMenu


class MenuAdmin(admin.ModelAdmin):
    fields = ['name', 'page', 'slug']
    list_display = ('name', 'page', 'slug')


class SubMenuAdmin(admin.ModelAdmin):
    fields = ['main_menu', 'submenu']
    list_display = ('main_menu', 'submenu')


admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
