from django.contrib import admin
from .models import Reklam, Brands, News, Category, UserReklam, SubCategory, Address, Color, Gender, Size, FirmReklam


@admin.register(Reklam)
class ReklamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'brand', 'category', 'subcategory',
                    'user', 'phone', 'address', 'price', 'count', 'text', 'created', 'kredit', 'obmen', 'ready')
    list_filter = ('name', 'price', 'created', 'brand', 'category')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    date_hierarchy = 'created'
    search_fields = ('name', )


@admin.register(FirmReklam)
class FirmReklamAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'email', 'web_address',
                    'created', 'address', 'text', 'phone', 'user')
    list_filter = ('name', 'created', 'user', 'phone')
    search_fields = ('name', )


admin.site.register(Brands)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(UserReklam)
admin.site.register(SubCategory)
admin.site.register(Address)
admin.site.register(Color)
admin.site.register(Gender)
admin.site.register(Size)


