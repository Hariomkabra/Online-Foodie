from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name
