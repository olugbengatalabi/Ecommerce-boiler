# Generated by Django 3.2.6 on 2021-12-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_remove_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
