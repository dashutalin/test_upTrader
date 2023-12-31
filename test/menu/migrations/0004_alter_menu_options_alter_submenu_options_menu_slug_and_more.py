# Generated by Django 4.2.6 on 2023-10-27 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_submenu_submenu_alter_submenu_main_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
        migrations.AlterModelOptions(
            name='submenu',
            options={'verbose_name': 'связь между пунктами меню', 'verbose_name_plural': 'Связи между пунктами меню'},
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(default=1, verbose_name='Слаг'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=30, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='page',
            field=models.CharField(max_length=30, verbose_name='страница'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='main_menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='menu.menu', verbose_name='родительский пунт'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='submenu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submenu', to='menu.menu', verbose_name='дочерний пункт'),
        ),
    ]
