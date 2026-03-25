from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)


    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Table"

class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self) :
        return self.name
    

class product(models.Model):
    image=models.ImageField(null=False,blank=False)
    name=models.CharField(max_length=200,null=False,blank=False)
    price= models.DecimalField(max_digits=5,decimal_places=2)
    description=models.TextField()
    is_published=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
     
    def __str__(self):
        return self.name

class Order(models.Model):
    uname= models.CharField(max_length=250)
    phone = models.TextField()
    address = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)


    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name_plural = "Order Table"