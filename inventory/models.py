from django.db import models

from utils.models import BaseModel


class Product(BaseModel):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_product_with_iva(self,iva = 19):
        return round(self.price * (1 + iva/100),2)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'
