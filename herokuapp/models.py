from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# https://docs.djangoproject.com/en/2.2/topics/db/sql/


class Customer(models.Model):
    id = models.AutoField
    cmnd = models.IntegerField(max_length=9,default=0)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    number_ticket = models.CharField(max_length=50)
    deposit = models.CharField(max_length=50)
    money = models.CharField(max_length=50)
    start_date = models.DateField()
    start_time_train = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
