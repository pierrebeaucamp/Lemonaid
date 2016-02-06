from django.db import models

class Debtor(models.Model):
    bank_key = models.CharField(blank=True, null=True, max_length=254)

