# Generated by Django 3.1.3 on 2020-11-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimordial_django', '0002_auto_20201113_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='分类"', max_length=50, verbose_name='分类'),
        ),
    ]
