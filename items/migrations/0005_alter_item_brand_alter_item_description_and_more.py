# Generated by Django 4.2 on 2023-06-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_detail_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(blank=True, help_text='opcional', max_length=50, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(help_text='Describe una lista de caracaterísticas principales', max_length=500, null=True, verbose_name='Descripcion corta'),
        ),
        migrations.AlterField(
            model_name='item',
            name='detail',
            field=models.TextField(blank=True, help_text='Datalla cada característica pricipal para los compradores', max_length=3000, null=True, verbose_name='Detalles'),
        ),
        migrations.AlterField(
            model_name='item',
            name='model',
            field=models.CharField(blank=True, help_text='opcional', max_length=50, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(help_text='Indicá producto, marca, modelo y características principales', max_length=100, null=True, verbose_name='Titulo'),
        ),
    ]
