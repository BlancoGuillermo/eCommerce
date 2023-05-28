from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="subcategory", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # ordena alfabéticamente
        verbose_name_plural = "Categories"


class Item(models.Model):
    category = models.ForeignKey(Category, verbose_name="Categoria", related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Titulo", blank=False)
    brand = models.CharField(max_length=50, verbose_name="Marca", blank=True)
    model = models.CharField(max_length=50, verbose_name="Modelo", blank=True)
    description = models.TextField(verbose_name="Descripcion", blank=False, null=True)
    price = models.DecimalField(verbose_name="Precio", max_digits=10, decimal_places=2)
    images = models.ImageField(verbose_name="Imagenes", upload_to="items_img", blank=False, null=True)
    condition = models.BooleanField(default='nuevo', verbose_name="Condicion", choices=((True , "nuevo"), (False, "usado")))
    sold = models.BooleanField(default=False)    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("items:detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name_plural = 'Items'
