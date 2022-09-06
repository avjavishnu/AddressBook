from django.db import models


# Create your models here.


class AddressBook(models.Model):
    Name_Student = models.CharField(max_length=50)
    Mobile_Number = models.IntegerField(null=False, blank=False)
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=40)
