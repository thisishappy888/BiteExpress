from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50, blank=False)
    images = models.CharField(max_length=250)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title

class Burgers(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.IntegerField(default=999)

    def __str__(self):
        return self.name

