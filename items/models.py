from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) # ordena alfabéticamente
        verbose_name_plural = "Categories"

    # devuelve string con el nombre de items
    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='item_img')


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=True) # puede quedar en blanco
    price = models.FloatField(blank=False)
    image = models.ManyToManyField(Image, related_name='items', blank=False)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # si se borra usuario también sus publicaciones lo harán
    created_at = models.DateTimeField(auto_now_add=True)

    # devuelve string con el nombre de items
    def __str__(self):
        return self.name
