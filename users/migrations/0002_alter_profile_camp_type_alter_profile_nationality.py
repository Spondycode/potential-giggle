# Generated by Django 4.1 on 2023-09-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='camp_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(max_length=50),
        ),
    ]
