from django.contrib import admin
from mysite.general.models import *

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')

class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'sel_cat')

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'sel_subcat')

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)