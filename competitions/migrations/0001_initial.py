# Generated by Django 4.1 on 2023-09-06 12:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'deliveries',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('collection', models.CharField(blank=True, max_length=500, null=True)),
                ('min_ticket', models.IntegerField(default=1)),
                ('max_ticket', models.IntegerField()),
                ('quantity_winners', models.IntegerField(default=1)),
                ('alternative_prize', models.CharField(blank=True, max_length=30, null=True)),
                ('end_date', models.DateField()),
                ('tickets_bought', models.IntegerField()),
                ('charity', models.CharField(max_length=60)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.delivery')),
                ('owner', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('correct_answer', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.product')),
            ],
        ),
    ]
