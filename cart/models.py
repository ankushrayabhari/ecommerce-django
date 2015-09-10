from django.db import models
from product.models import *
from authenticate.models import *

# Create your models here.
class CartItem(models.Model):
	product = models.ManyToManyField(Product)
	quantity = models.IntegerField()
	customer = models.ForeignKey(Customer, null=True)

	def __str__(self):
		return self.product.name