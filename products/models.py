from django.db import models




class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


