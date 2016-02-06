# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lemonaid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('flow_type', models.CharField(choices=[('e', 'Expense'), ('i', 'Income')], max_length=254)),
                ('duration_type', models.CharField(choices=[('m', 'Monthly Amount'), ('a', 'Annual Amount')], max_length=254)),
                ('amount', models.FloatField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lemonaid.UserProfile')),
            ],
        ),
    ]
