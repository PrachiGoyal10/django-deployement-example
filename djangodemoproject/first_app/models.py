from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    Email = models.CharField(max_length=250,unique=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

