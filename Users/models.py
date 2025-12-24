from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    telefon_raqam = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(default=2)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)


    REQUIRED_FIELDS = ["age", "telefon_raqam"]
    
    
    


    def __str__(self):
        return self.telefon_raqam