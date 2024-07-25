from django.db import models

from config.settings import NULLABLE


class NetworkChain(models.Model):
    """
    Модель Поставщика
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    supplier = models.ForeignKey("self", on_delete=models.CASCADE, **NULLABLE, verbose_name="Поставщик")
    debt_amount = models.DecimalField(
        **NULLABLE,
        max_digits=30,
        decimal_places=2,
        verbose_name="Задолженность перед поставщиком",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    """
    Модель Продукта
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    model = models.CharField(max_length=30, **NULLABLE, verbose_name="Модель")
    market_date = models.DateField(verbose_name="Дата выхода на рынок")
    seller = models.ForeignKey(NetworkChain, on_delete=models.CASCADE, **NULLABLE, verbose_name="Продавец")

    def __str__(self) -> str:
        return f"{self.name}"


class Contact(models.Model):
    """
    Модель Контакта
    """

    email = models.EmailField(max_length=50, verbose_name="Email")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, **NULLABLE, verbose_name="Улица")
    building = models.CharField(max_length=50, **NULLABLE, verbose_name="Номер дома")
    seller = models.ForeignKey(NetworkChain, on_delete=models.CASCADE, **NULLABLE, verbose_name="Продавец")

    def __str__(self) -> str:
        return f"{self.country}"
