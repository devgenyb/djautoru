# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class New(models.Model):
    price = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    engine = models.CharField(max_length=100, blank=True, null=True)
    tax = models.CharField(max_length=100, blank=True, null=True)
    gearbox = models.CharField(max_length=100, blank=True, null=True)
    wd = models.CharField(max_length=100, blank=True, null=True)
    complectation = models.CharField(max_length=100, blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    manufakturer = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'new'
    def __str__(self):
        return self.manufakturer + ' ' + self.model

class Used(models.Model):
    price = models.CharField(max_length=100, blank=True, null=True)
    relise_year = models.CharField(max_length=100, blank=True, null=True)
    kmage = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    engine = models.CharField(max_length=100, blank=True, null=True)
    tax = models.CharField(max_length=100, blank=True, null=True)
    gearbox = models.CharField(max_length=100, blank=True, null=True)
    wd = models.CharField(max_length=100, blank=True, null=True)
    wheel = models.CharField(max_length=100, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=True)
    owners = models.CharField(max_length=100, blank=True, null=True)
    pts = models.CharField(max_length=100, blank=True, null=True)
    owning = models.CharField(max_length=100, blank=True, null=True)
    customs = models.CharField(max_length=100, blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    manufakturer = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'used'

    def __str__(self):
        return self.manufakturer + self.model
