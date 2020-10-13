from django.db import models


class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    type = models.CharField(max_length=100, default='purchase')
    remark = models.CharField(max_length=1000,default='')


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


class Job(models.Model):
    no = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateField()
    is_done = models.PositiveSmallIntegerField()
    is_paid = models.PositiveSmallIntegerField()
