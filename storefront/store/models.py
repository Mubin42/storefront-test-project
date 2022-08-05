import email
from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    price       = models.DecimalField(max_digits=6,decimal_places=2) #for decimal value always use decimal fields
    inventory   = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEBERSHIP_BRONZE = 'B'
    MEBERSHIP_SILVER = 'S'
    MEBERSHIP_GOLD   = 'G'

    MEMBERSHIP_CHOICES = [
        (MEBERSHIP_BRONZE, 'Bronze'),
        (MEBERSHIP_SILVER, 'Silver'),
        (MEBERSHIP_GOLD,   'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEBERSHIP_BRONZE)


class Order(models.Model):
    STATUS_PENDING  = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILED   = 'F'
    
    STATUS_CHOICE = [
        (STATUS_PENDING,   'Pending'),
        (STATUS_COMPLETE,  'Complete'),
        (STATUS_FAILED,    'Failed'),
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=STATUS_PENDING)
