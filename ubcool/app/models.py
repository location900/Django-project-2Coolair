from django.db import models


class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class WarrantyQuote(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    product = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    date = models.DateField()
    under_warranty = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=10000)
