from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    page = models.CharField(max_length=30, verbose_name='страница')
    slug = models.SlugField(verbose_name='Слаг')

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    main_menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                                  related_name='menu', verbose_name='родительский пунт')
    submenu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                                related_name='submenu', verbose_name='дочерний пункт')

    class Meta:
        verbose_name = 'связь между пунктами меню'
        verbose_name_plural = 'Связи между пунктами меню'

    def __str__(self):
        return self.main_menu.name
