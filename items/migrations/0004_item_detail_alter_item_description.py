# Generated by Django 4.2 on 2023-06-05 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='detail',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Detalles'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Descripcion'),
        ),
    ]
