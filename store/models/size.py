from django.db import models
from django.contrib.auth.models import User
from .tshirt import Tshirt

class SizeVariant(models.Model):
    SIZES = (
        ('S' , "Small"), 
        ('M' , "Medium"), 
        ('L' , "Large"), 
        ('XL' , "Extra Large"), 
        ('XXL' , "Extra Extra Large"), 
    )
    price = models.IntegerField(null = False)
    tshirt = models.ForeignKey(Tshirt , on_delete=models.CASCADE)
    size = models.CharField(choices=SIZES , max_length=5)

    def __str__(self):
        return f'{self.size}'