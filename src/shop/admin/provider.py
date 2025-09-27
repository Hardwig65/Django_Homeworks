from shop.models import Provider,Product
from django.contrib import admin

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name','country','zip_address')
    inlines = (ProductInline,)


provider_admin = admin.site.register(Provider, ProviderAdmin)