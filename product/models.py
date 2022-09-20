from django.db import models

class Users(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name
        
        
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    rate = models.FloatField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name
        
        
