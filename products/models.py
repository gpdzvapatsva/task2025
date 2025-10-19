from django.db import models
import datetime


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=20)
    product_description = models.CharField(max_length=20, null=True)
    product_id = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=6, decimal_places=2, max_length=8)
    '''date_purchased=models.DecimalField(max_digits=6, decimal_places=2, max_length=8)'''
    prod_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f'{self.name},{self.product_description}, {self.product_id}, {self.quantity},{self.cost}, {self.prod_image}'

    class Meta:
        verbose_name_plural = 'Products'
