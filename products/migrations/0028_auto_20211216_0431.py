# Generated by Django 3.2.6 on 2021-12-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20211211_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SW', 'Sports Wear'), ('S', 'shirt'), ('OW', 'Outwear')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('D', 'danger'), ('S', 'secondary')], max_length=1),
        ),
    ]
