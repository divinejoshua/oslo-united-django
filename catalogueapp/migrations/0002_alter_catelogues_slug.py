# Generated by Django 3.2.5 on 2021-07-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogueapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catelogues',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]