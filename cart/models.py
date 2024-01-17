from django.db import models

# Create your models here.

class address(models.Model):
    name = models.CharField(max_length=20)
    mob = models.IntegerField(primary_key=True)
    gmail = models.EmailField()
    house_no = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pin = models.IntegerField()
    state = models.CharField(max_length=20)

