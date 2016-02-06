from django.db import models

from django.contrib.auth.models import User

from datetime import timedelta

# Create your models here.

class UserProfile(models.Model):
    TITLE_CHOICES = (
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('ms', 'Ms'),
        ('miss', 'Miss'),
    )

    MARITAL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
    )

    RESIDENTIAL_STATUS_CHOICES = (
        ('own', 'Own'),
        ('rent', 'Rent'),
        ('lease', 'Lease'),
    )

    user = models.OneToOneField(User)

    bank_key = models.CharField(blank=True, null=True, max_length=254)
    title = models.CharField(max_length=254, choices=TITLE_CHOICES)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=254, choices=MARITAL_STATUS_CHOICES)
    sin = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    province = models.CharField(max_length=254)
    postal_code = models.CharField(max_length=6)
    residential_status = models.CharField(max_length=254, choices=RESIDENTIAL_STATUS_CHOICES)

    creditor_balance = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Flow(models.Model):
    DURATION_TYPE_CHOICES = (
        ('m', 'Monthly Amount'),
        ('a', 'Annual Amount'),
    )

    FLOW_TYPE_CHOICES = (
        ('e', 'Expense'),
        ('i', 'Income'),
    )

    profile = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=254)
    flow_type = models.CharField(max_length=254, choices=FLOW_TYPE_CHOICES)
    duration_type = models.CharField(max_length=254, choices=DURATION_TYPE_CHOICES)
    amount = models.FloatField()


class Loan(models.Model):
    profile = models.ForeignKey(UserProfile)
    amount = models.FloatField()
    interest = models.FloatField()
    duration = models.DurationField(default=timedelta(weeks=52))


