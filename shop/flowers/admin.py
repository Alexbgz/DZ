from django.contrib import admin
from .models import Catalog, Order

# Register your models here.


class PostCatalog(admin.ModelAdmin):
    list_display = ('product', 'category', 'price', 'quantity', 'foto', 'image_img')
    list_filter = ('category',)
    search_fields = ['product']
    readonly_fields = ['image_img', ]

admin.site.register(Catalog, PostCatalog)


class PostOrder(admin.ModelAdmin):
    list_display = ('id', 'iduser', 'idproduct', 'quantity', 'summ')

admin.site.register(Order, PostOrder)