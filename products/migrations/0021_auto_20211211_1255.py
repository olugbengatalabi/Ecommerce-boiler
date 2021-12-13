# Generated by Django 3.2.6 on 2021-12-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20211211_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SW', 'Sports Wear'), ('OW', 'Outwear'), ('S', 'shirt')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1),
        ),
    ]