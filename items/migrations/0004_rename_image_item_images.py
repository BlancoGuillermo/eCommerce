# Generated by Django 4.2 on 2023-05-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_image_alter_item_description_remove_item_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='images',
        ),
    ]
