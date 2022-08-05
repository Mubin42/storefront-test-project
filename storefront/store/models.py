import email
from django.db import models

#ManyToMany
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

#OneToMany Relations
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    price       = models.DecimalField(max_digits=6,decimal_places=2) #for decimal value always use decimal fields
    inventory   = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection  = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions  = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD   = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD,   'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    STATUS_PENDING  = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILED   = 'F'
    
    STATUS_CHOICE = [
        (STATUS_PENDING,   'Pending'),
        (STATUS_COMPLETE,  'Complete'),
        (STATUS_FAILED,    'Failed'),
    ]
    
    placed_at      = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=STATUS_PENDING)
    customer       = models.ForeignKey(Customer, on_delete=models.PROTECT)

#OneToMany
class OrderItem(models.Model):
    order      = models.ForeignKey(Order, on_delete=models.PROTECT)
    product    = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity   = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

#OneToOne relations
class Address(models.Model):
    street   =  models.CharField(max_length=255)
    city     =  models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE, primary_key=True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


