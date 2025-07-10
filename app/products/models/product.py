from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название продукта"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Описание"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена"))
    banner_photo = models.ImageField(
        upload_to='products/banners/%Y/%m',
        blank=True, verbose_name=_("Баннер")
    )
    categories = models.ManyToManyField(
        'Category', blank=True, related_name='products', verbose_name=_("Категории")
    )
    tags = models.ManyToManyField(
        'Tag', blank=True, related_name='products', verbose_name=_("Теги")
    )
    is_hidden = models.BooleanField(default=False, verbose_name=_("Скрыт"))
    is_bestseller = models.BooleanField(default=False, verbose_name="Бестселлер")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos', verbose_name=_("Продукт"))
    photo = models.ImageField(
        upload_to='products/gallery/%Y/%m',
        verbose_name=_("Фото")
    )
    alt = models.CharField(max_length=255, blank=True, verbose_name=_("ALT-текст"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        verbose_name = _("Фото товара")
        verbose_name_plural = _("Фотографии товаров")
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.product.name} — {self.alt or self.photo.name}"


class ProductColorPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='color_photos')
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products/colors/%Y/%m', verbose_name=_("Фото"))
    alt = models.CharField(max_length=255, blank=True, verbose_name=_("ALT-текст"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'id']
        verbose_name = _("Фото цветового варианта товара")
        verbose_name_plural = _("Фотографии цветовых вариантов товаров")

    def __str__(self):
        return f"{self.product.name} - {self.color.name} — {self.alt or self.photo.name}"
