from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    author = models.CharField(max_length=100, default="Unknown")
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"{self.author} - {self.product.name}"


