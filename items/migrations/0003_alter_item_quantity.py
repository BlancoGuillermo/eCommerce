# Generated by Django 4.2 on 2023-06-05 00:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Para que un artículo esté disponible, el stock debe ser mayor a 0'), django.core.validators.MaxValueValidator(100, 'No puedes publicar un artículo con stock mayor a 100 unidades')], verbose_name='Stock'),
        ),
    ]
