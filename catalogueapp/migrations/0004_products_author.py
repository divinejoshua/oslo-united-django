# Generated by Django 3.2.5 on 2021-07-14 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogueapp', '0003_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalogueapp.catelogues'),
        ),
    ]
