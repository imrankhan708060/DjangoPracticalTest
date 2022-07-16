from django.db import models
from . managers import  CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _



'''
Custom user
'''

class CustomUser(AbstractUser):
    email = models.EmailField(_('Email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    price = models.FloatField()
    photo = models.FileField()
    description = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.name

class CartItem(models.Model):
    item_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    item_count = models.IntegerField(default=0)

    def __str__(self):

        return self.item_product.name
