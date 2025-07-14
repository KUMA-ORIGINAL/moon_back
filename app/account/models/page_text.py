from django.db import models


class PageText(models.Model):
    key = models.CharField(max_length=100, unique=True, help_text="Уникальный ключ для текста, например 'home.title'")
    text = models.TextField("Текст", blank=True, null=True)
    image_url = models.URLField("Ссылка на изображение", blank=True, null=True)

    def __str__(self):
        return f"{self.key}: {self.text[:30]}"


class PageTextGlobalVersion(models.Model):
    version = models.PositiveIntegerField(default=1)

    @classmethod
    def bump(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        obj.version += 1
        obj.save()
        return obj.version

    @classmethod
    def current(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj.version
