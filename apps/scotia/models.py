from django.db import models

# Create your models here.

class Debtor(models.Model):
    bank_key = models.CharField(blank=True, null=True, max_length=254)

