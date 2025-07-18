# Generated by Django 5.1 on 2025-06-15 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_banner_photo_alter_productphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.CreateModel(
            name='ProductColorPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='products/colors/%Y/%m', verbose_name='Фото')),
                ('alt', models.CharField(blank=True, max_length=255, verbose_name='ALT-текст')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_photos', to='products.product')),
            ],
            options={
                'verbose_name': 'Фото цветового варианта товара',
                'verbose_name_plural': 'Фотографии цветовых вариантов товаров',
                'ordering': ['order', 'id'],
            },
        ),
    ]
