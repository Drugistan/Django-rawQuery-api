from django.db import models


# Create your models here.


class Customers(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=200)
    last_name = models.CharField(blank=True, null=True, max_length=200)
    phone = models.CharField(blank=True, null=True, max_length=200)
    email = models.EmailField(blank=True, null=True)
    state = models.CharField(blank=True, null=True, max_length=200)


class Orders(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="order_customer", blank=True,
                                  null=True)
    order_id = models.CharField(blank=True, null=True, max_length=200, unique=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    orderCreatedAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    orderUpdatedAt = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
