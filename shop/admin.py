from django.contrib import admin

from .models import Product, Category


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'category', 'price',
                    'available']
    search_fields = [
        'name', 'description',
    ]
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
