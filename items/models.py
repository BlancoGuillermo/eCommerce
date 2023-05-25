<<<<<<< HEAD
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
    sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(verbose_name="Imagenes", blank=False, null=True)
    condition = models.BooleanField(default='nuevo', verbose_name="Condicion", choices=((True , "nuevo"), (False, "usado")))
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("item:detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name_plural = 'Items'
=======
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


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) # puede quedar en blanco
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True) # blank y null debería ser False para impedir crear items sin imagen
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # si se borra usuario también sus publicaciones lo harán
    created_at = models.DateTimeField(auto_now_add=True)

    # devuelve string con el nombre de items
    def __str__(self):
        return self.name
>>>>>>> main
