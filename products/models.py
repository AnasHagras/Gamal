from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

class Product (models.Model):
    name = models.CharField(max_length = 100)
    content = models.TextField()
    price = models.DecimalField(max_digits = 6 , decimal_places = 2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    
    def __str__ (self):
        return self.name

    class Meta: 
        ordering = ['name','active']

    def __name__ (self):
        return  
        
class User (models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
    products = models.ForeignKey(Product,on_delete=models.CASCADE)

class Female(models.Model):
    name_female = models.CharField(max_length=50,null=True)
    def __str__ (self):
        return self.name_female

class Male(models.Model):
    name_male = models.CharField(max_length=50,null=True)
    girls = models.OneToOneField(Female,on_delete=models.CASCADE)
    def __str__ (self):
        return self.name_male

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)