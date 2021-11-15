from django.contrib import admin
from .models import GetInTouch, Blogs, Menu, Customer, Order, OrderItem

# Register your models here.

admin.site.register(GetInTouch)
admin.site.register(Blogs)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Order)