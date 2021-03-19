from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name =models.OneToOneField(User,on_delete= models.CASCADE)
    image = models.ImageField(default = "default.jpg",upload_to="media")

    def __str__(self):
        return str(self.name.username)
