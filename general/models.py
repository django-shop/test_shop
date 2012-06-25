# -*- coding: utf-8 -*-
from django.db import models

class ProductType:
    name = models.CharField(max_length=200)

class ProductParameter:
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField()
    type = models.ForeignKey(ProductType)
    parameters = models.ManyToManyField(ProductParameter, through='ProductParameterValue')

class ProductParameterValue:
    parameter = models.ForeignKey(ProductParameter)
    product = models.ForeignKey(Product)
    Value = models.CharField(max_length=200)




