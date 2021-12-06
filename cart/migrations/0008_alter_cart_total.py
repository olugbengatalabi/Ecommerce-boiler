# Generated by Django 3.2.6 on 2021-12-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
