# Generated by Django 4.2 on 2023-05-23 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='images',
            field=models.ImageField(null=True, upload_to='item_images/', verbose_name='Imagenes'),
        ),
        migrations.DeleteModel(
            name='ImageItem',
        ),
    ]
