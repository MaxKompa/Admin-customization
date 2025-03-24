from django.contrib import admin
from .models import Product, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "status", "created_at", "review_count")
    inlines = [ReviewInline]

    def review_count(self, obj):
        return obj.reviews.count()
    review_count.short_description = "Кількість відгуків"
