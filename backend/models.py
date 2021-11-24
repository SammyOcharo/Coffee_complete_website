from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class GetInTouch(models.Model):
    Title = models.CharField(max_length=50, blank=False, null=True)
    Email = models.EmailField(blank=False, null=True)
    Number = models.IntegerField(blank=False, null=True)


class Blogs(models.Model):
    Images = models.ImageField(upload_to = './backend/static/media/')
    Title = models.CharField(max_length=50)
    Writer = models.CharField(max_length=50)
    Date = models.DateField(auto_created=True)
    Details = models.TextField()

    def __str__(self):
        return self.Title
    
class Menu(models.Model):
    Coffee_image = models.ImageField(upload_to = './backend/static/media/')
    Coffee_name = models.CharField(max_length=60)
    Cost = models.FloatField()
    Discounted_Cost = models.FloatField()

    def __str__(self):
        return self.Coffee_name

class Customer(models.Model):
    user= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_Id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.customer)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.Discounted_Cost * self.quantity
        return total




