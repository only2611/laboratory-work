from django.db import models

# Create your models here.


# Create your models here.
CATEGORY = [('milk', 'Молочные'), ('organic', 'Органические'), ('fast_feed', 'Быстрого приготовления'),
            ('drinks', 'Напитки'),('vegetables', 'Овощи'), ('other', 'Разное')]

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование товара")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    categories = models.CharField(max_length=100, choices=CATEGORY, verbose_name="Категория", default="other")
    balance = models.PositiveIntegerField(verbose_name="Остаток товара")
    price = models.DecimalField(max_length=100, max_digits=7, decimal_places=2, verbose_name="Цена товара")


    def __str__(self):
        return f"{self.id}.{self.name} - {self.description} - {self.categories}"


    class Meta:
        db_table = "market"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"