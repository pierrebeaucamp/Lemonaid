from django.db import models
from django.forms import FloatField

from django.contrib.auth.models import User

from datetime import timedelta

# Create your models here.
from django.db.models import Count, Sum, F


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

    USER_TYPE_CHOICES = (
        ('d', 'debtor'),
        ('c', 'creditor'),
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
    type = models.CharField(max_length=254, choices=USER_TYPE_CHOICES)
    creditor_balance = models.FloatField(default=0)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def get_single_loan_total(self):
        total_sum = 0
        if self.type == 'c':
            loans = SingleLoan.objects.filter(creditor=self)
            if loans:
                total_sum = loans.aggregate(total_sum=Sum(F('amount')))['total_sum']
        return total_sum


class CashFlow(models.Model):
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
    amount = models.FloatField(default=0)
    date = models.DateField()


class SingleLoan(models.Model):
    # creditors
    creditor = models.OneToOneField(UserProfile, null=True, related_name='single_creditor')
    debitor = models.OneToOneField(UserProfile, null=True, related_name='single_debitor')
    amount = models.FloatField(default=0)
    interest = models.FloatField(default=0)
    duration = models.DurationField(default=timedelta(weeks=52))
    debitor_loan = models.ForeignKey('DebitorLoan', null=True)

    def deduct_amount(self):
        self.debitor_loan.amount = self.debitor_loan.amount - self.amount
        print("Printing this {}".format(self.debitor_loan.amount))
        self.creditor.creditor_balance = self.creditor.creditor_balance - self.amount
        print("Printing this {}".format(self.creditor.creditor_balance))
        self.debitor_loan.save()
        self.creditor.save()


class PoolLoan(models.Model):
    # creditors
    creditor = models.ManyToManyField(UserProfile, null=True, related_name='pool_creditor')
    amount = models.FloatField(default=0)
    interest = models.FloatField(default=0)
    duration = models.DurationField(default=timedelta(weeks=52))
    debitor_loan = models.ForeignKey('DebitorLoan', null=True)

    def deduct_amount(self):


        distrubited_creditor_amount = self.amount / self.creditor.count()
        for c in self.creditor:
            c.creditor_balance = c.creditor_balance - distrubited_creditor_amount
        self.debitor_loan.amount = self.debitor_loan.amount - self.amount
        self.debitor_loan.save()
        self.creditor.save()


class Pool(models.Model):
    TYPE_CHOICES = (
        ('l', 'Low'),
        ('m', 'Medium'),
        ('h', 'High'),
    )
    type = models.CharField(max_length=254, choices=TYPE_CHOICES, default='Low')
    interest_rate = models.FloatField(default=0)
    amount = models.FloatField(default=0)

class DebitorLoan(models.Model):
    amount = models.FloatField(default=0)
    debitor = models.OneToOneField(UserProfile)
