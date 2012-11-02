__author__ = 'dextraz'
from django.contrib import admin
from models import Product
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category','name')}
    list_display = ('sku','category','name','description','price','old_price','new_price','in_stock','date_added')
    list_editable = ('in_stock','name')
    list_filter = ('category','name')
    list_display_links = ('category','description')
    search_fields = ('name',)



admin.site.register(Product,ProductAdmin)