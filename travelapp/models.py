from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(null=True)
    def __str__(self):
        return self.name
class Peoples(models.Model):
    img = models.ImageField(upload_to='pics/people')
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True)
    def __str__(self):
        return self.name
