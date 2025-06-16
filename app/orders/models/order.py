from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'ожидание', 'Ожидает'
        PAID = 'оплачен', 'Оплачен'
        CANCELLED = 'отменен', 'Отменен'

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Общая стоимость"
    )
    status = models.CharField(
        max_length=50,
        choices=Status,
        default=Status.PENDING,
        verbose_name="Статус платежа",
        blank=True,
        null=True
    )
    first_name = models.CharField("Имя", max_length=64)
    last_name = models.CharField("Фамилия", max_length=64)
    company = models.CharField("Компания", max_length=128, blank=True)  # Необязательное поле
    country = models.CharField("Страна / регион", max_length=64)
    street_address = models.CharField("Адрес", max_length=255)
    city = models.CharField("Город", max_length=64)
    state = models.CharField("Область / район", max_length=64)
    zip_code = models.CharField("Почтовый индекс", max_length=32, blank=True)  # Необязательное поле
    phone = models.CharField("Телефон", max_length=32)
    email = models.EmailField("Email", blank=True)  # Необязательное поле
    order_notes = models.TextField("Комментарий к заказу", blank=True)  # Необязательное поле

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    def __str__(self):
        return f"Заказ №{self.id} от {self.first_name} {self.last_name}"

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
