from django.contrib import admin
from .models import Product, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Базовая кастомизация
    list_display = ('name', 'price', 'status', 'created_at')  # Поля в списке объектов
    list_filter = ('status', 'created_at')  # Фильтрация
    search_fields = ('name', 'description')  # Поля для поиска

    # Расширенная кастомизация
    ordering = ('-created_at',)  # Сортировка по дате создания (от новых к старым)
    list_editable = ('status',)  # Позволяет редактировать статус прямо в списке
    list_per_page = 10  # Количество объектов на странице

    readonly_fields = ('created_at',)


# Группировка полей в форме редактирования
    fieldsets = (
        ('Основная информация', {'fields': ('name', 'description')}),
        ('Финансы', {'fields': ('price',)}),
        ('Дополнительные настройки', {'fields': ('status',)}),
    )

    # Валидация (пример проверки будущей даты)
    def save_model(self, request, obj, form, change):
        if obj.created_at and obj.created_at > timezone.now():
            raise ValueError("Дата создания не может быть в будущем!")
        super().save_model(request, obj, form, change)


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # Количество пустых полей для добавления новых отзывов

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_at', 'review_count')  # Добавляем колонку с количеством отзывов
    inlines = [ReviewInline]

    def review_count(self, obj):
        return obj.reviews.count()
    review_count.short_description = "Количество отзывов"
