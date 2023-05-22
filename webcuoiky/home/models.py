from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

#s ok
class Customer(models.Model):
    class Meta:
        ordering = ['-id']
        
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    email = models.EmailField(default=None)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
# ok
class Category(models.Model):
    class Meta:
        ordering = ['-id']

    name = models.CharField(max_length=200, null=False)
    images = models.ImageField(upload_to='category/%Y/%m', default=None)

    def __str__(self):
        return self.name

# ok
class Product(models.Model):
    class Meta:
        ordering = ['-id']

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    descriptions = models.TextField(default=None)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_Date = models.DateTimeField(default=timezone.now)
    images = models.ImageField(upload_to='product/%Y/%m', default=None)        

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    created_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

    
    
class OrderItem(models.Model):
    class Meta:
        ordering = ['-id']

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product.name




