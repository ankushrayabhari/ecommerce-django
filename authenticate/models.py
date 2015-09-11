from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User)
    
    def __str__(self):
        return self.user.username
