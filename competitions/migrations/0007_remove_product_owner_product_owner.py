# Generated by Django 4.1 on 2023-09-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0006_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.TextField(default='OWNER'),
        ),
    ]
