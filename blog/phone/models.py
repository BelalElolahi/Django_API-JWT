from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Phone(models.Model) :
    phone_name =models.CharField(max_length=55)
    phone_descrption = models.TextField()
    phone_id = models.IntegerField()
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE) 