from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import (
Product,
)


@admin.action(description="Make product unavailable")
def make_unavailable(modeladmin, request, queryset):
    queryset.update(is_available = False)



class ProductAdmin(admin.ModelAdmin):

    fieldsets = (('Основная информация',{"fields":('name','price','category', 'is_available', 'count_items')}),
                 ('Фото и описание',{'fields':('photo', 'description'), 'classes':('collapse',)}),
                 ('Поставщик',{'fields':('provider',)}))
    list_display = ('name', 'price', 'is_available', 'category', 'count_items','photo', 'image_preview')
    list_filter = ('category', 'is_available')
    search_fields = ('name','description')
    list_editable = ('is_available','price')
    readonly_fields = ('image_preview',)
    list_filter = ('provider',)

    def image_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150" height="150" />')
        return 'Нет изображения'
    actions = [make_unavailable]


product_admin = admin.site.register(Product, ProductAdmin)


from shop.models import (
    Order,
    Feedback,
    ProductDetail,
    ProductOrder,
    ProductRating,
    ProviderRating,
    Rating
)

admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(ProductDetail)
admin.site.register(ProductOrder)
admin.site.register(ProductRating)
admin.site.register(ProviderRating)
admin.site.register(Rating)


