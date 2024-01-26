from django.db import models

class Person(models.Model):
    inn = models.CharField(max_length=10)
    last_name = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    surname= models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    passport_ser = models.CharField(max_length=2)
    passport_num = models.CharField(max_length=6)
