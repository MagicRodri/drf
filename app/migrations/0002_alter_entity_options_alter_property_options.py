# Generated by Django 4.1.4 on 2022-12-21 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name_plural': 'Entities'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
    ]
