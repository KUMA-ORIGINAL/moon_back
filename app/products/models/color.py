from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название цвета')
    hex_code = models.CharField(max_length=7, verbose_name='HEX-код', help_text='Например, #ffffff')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ['name']

    def __str__(self):
        return self.name

