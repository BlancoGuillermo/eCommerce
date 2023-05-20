import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',) # ordena alfabéticamente
        verbose_name_plural = "Categories"


def image_upload_custom(instance, filename):
    item_directory = f'item_{instance.pk}'
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'{instance.pk}_{timestamp}{os.path.splitext(filename)[1]}'
    return os.path.join('item_images', item_directory, filename)


class Item(models.Model):
    category = models.ForeignKey(Category, verbose_name="Categoria", related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Titulo", unique=True, blank=False)
    brand = models.CharField(max_length=50, verbose_name="Marca", unique=True, blank=True)
    model = models.CharField(max_length=50, verbose_name="Modelo", unique=True, blank=True)
    description = models.TextField(verbose_name="Descripcion", blank=False, null=True)
    price = models.FloatField(verbose_name="Precio", blank=False)
    sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    images = models.ImageField(upload_to=image_upload_custom, verbose_name="Imagenes", null=True, blank=False)

    def __str__(self):
        return self.name
