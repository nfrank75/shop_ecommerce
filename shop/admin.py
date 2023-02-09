from django.contrib import admin
# from django.contrib.admin import ModelAdmin
from .models import Category, Article, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'active',
        'created_at',
        'updated_at',
        )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'category',
        'active',
        'created_at',
        'updated_at',
        )


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'product',
        'active',
        'created_at',
        'updated_at',
        )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Article, ArticleAdmin)
