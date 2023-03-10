from django.db import models
from django.contrib.auth.models import User

class CustomCl(models.Model):
    name =models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TagCl(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductCl(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TagCl)

    def __str__(self):
        return self.name
class OrderCl(models.Model):
    STATUS = (
        ('На обработке', 'На обработке'),
        ('Выехал', 'Выехал'),
        ('Доставлен', 'Доставлен')
    )
    customer = models.ForeignKey(CustomCl, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCl, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.product.name