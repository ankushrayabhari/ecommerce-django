from django.db import models

# Create your models here.
class Product(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=25)
	description = models.CharField(max_length=3000)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	image = models.CharField(max_length=3000, null=True)

	def __str__(self):
		return self.name