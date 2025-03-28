from django.contrib import admin
from listings.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "shu", "price", "available")
    list_filter = ("available", "category")
    list_editable = ("price", "available")
    prepopulated_fields = {"slug": ("name",)}
