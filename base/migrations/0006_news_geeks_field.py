# Generated by Django 4.0.3 on 2022-03-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='geeks_field',
            field=models.URLField(blank=True, db_index=True, unique=True),
        ),
    ]
