from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    status = models.BooleanField(default=True, verbose_name="Активний")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField(verbose_name="Текст відгуку")
    rating = models.PositiveSmallIntegerField(verbose_name="Оцінка", default=5)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")



