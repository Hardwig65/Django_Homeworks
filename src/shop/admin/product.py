from django.contrib import admin

from shop.models import (
Product,
)

class ProductAdmin(admin.ModelAdmin):
    #fields = ('name', 'description', 'photo', ('count_items','price'))
    fieldsets = (
        (
            None,
            {
                'fields': ('name', ('count_items', 'price')),
            },
        ),
        (
            "Дополнительные поля",
            {
                'classes': ('collapse',),
                'fields': ['photo', 'description'],
            },
        ),
    )
    list_display = ('name', 'description','category', 'price', 'count_items', 'is_available')
    list_display_links = ('name', 'description',)
    list_editable = ('price','is_available','count_items')
    list_per_page = 10
    list_filter = ('category',)
    search_fields = ('name','price')



product_admin = admin.site.register(Product, ProductAdmin)


from django.contrib import admin
from shop.models import (
    Order,
    Feedback,
    ProductDetail,
    Provider,
    ProductOrder
)

admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(ProductDetail)
admin.site.register(Provider)
admin.site.register(ProductOrder)