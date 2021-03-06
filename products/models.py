from django.db import models
from django.db.models.fields import CharField, FloatField, SlugField

# Category Model

class Category(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

# Product Model

class Product(models.Model):
    name = CharField(max_length=300)
    slug = SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',blank=True)
    excerpt = models.TextField(max_length=200,verbose_name='Extracto')
    detail = models.TextField(max_length=1000,verbose_name='Información del Producto')
    price = FloatField()
    aviable = models.BooleanField(default=True)
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:    
        db_table= 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']