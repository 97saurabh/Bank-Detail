from django.db import models

# Create your models here.


class bankDetails(models.Model):
    ifsc = models.CharField(unique=True,max_length = 11)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length = 25)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 25)
    district = models.CharField(max_length = 25)
    state = models.CharField(max_length = 25)
    bank_name = models.CharField(max_length = 75)


