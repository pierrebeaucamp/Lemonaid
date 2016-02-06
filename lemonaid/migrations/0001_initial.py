# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 07:57
from __future__ import unicode_literals

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
            name='CashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('flow_type', models.CharField(choices=[('e', 'Expense'), ('i', 'Income')], max_length=254)),
                ('duration_type', models.CharField(choices=[('m', 'Monthly Amount'), ('a', 'Annual Amount')], max_length=254)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DebitorLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('l', 'Low'), ('m', 'Medium'), ('h', 'High')], default='Low', max_length=254)),
                ('interest_rate', models.FloatField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PoolLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('interest', models.FloatField()),
                ('duration', models.DurationField(default=datetime.timedelta(364))),
            ],
        ),
        migrations.CreateModel(
            name='SingleLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('interest', models.FloatField()),
                ('duration', models.DurationField(default=datetime.timedelta(364))),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_key', models.CharField(blank=True, max_length=254, null=True)),
                ('title', models.CharField(choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('ms', 'Ms'), ('miss', 'Miss')], max_length=254)),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=254)),
                ('sin', models.CharField(blank=True, max_length=9, null=True)),
                ('address', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('province', models.CharField(max_length=254)),
                ('postal_code', models.CharField(max_length=6)),
                ('residential_status', models.CharField(choices=[('own', 'Own'), ('rent', 'Rent'), ('lease', 'Lease')], max_length=254)),
                ('type', models.CharField(choices=[('d', 'debtor'), ('c', 'creditor')], max_length=254)),
                ('creditor_balance', models.FloatField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='singleloan',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lemonaid.UserProfile'),
        ),
        migrations.AddField(
            model_name='poolloan',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lemonaid.UserProfile'),
        ),
        migrations.AddField(
            model_name='debitorloan',
            name='pool_loan',
            field=models.ManyToManyField(blank=True, null=True, to='lemonaid.PoolLoan'),
        ),
        migrations.AddField(
            model_name='debitorloan',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lemonaid.UserProfile'),
        ),
        migrations.AddField(
            model_name='debitorloan',
            name='single_loan',
            field=models.ManyToManyField(blank=True, null=True, to='lemonaid.SingleLoan'),
        ),
        migrations.AddField(
            model_name='cashflow',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lemonaid.UserProfile'),
        ),
    ]
