from django.contrib import admin
from .models import Product,Category,Brand
# Register your models here.

admin.site.register(Brand)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)