# Generated by Django 3.2.6 on 2021-12-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20211206_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('S', 'shirt'), ('SW', 'Sports Wear'), ('OW', 'Outwear')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('S', 'secondary'), ('P', 'primary')], max_length=1),
        ),
    ]
