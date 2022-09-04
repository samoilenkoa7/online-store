from django.contrib import admin
from .models import Account, PostsImages, UserOrder


class ImageInline(admin.TabularInline):
    model = PostsImages


class AdminAccountView(admin.ModelAdmin):
    list_display = ('title', 'level', 'outfits', 'gliders_amount', 'acc_price')
    list_filter = ['title', 'level', 'outfits']
    inlines = [ImageInline]


admin.site.register(Account, AdminAccountView)
admin.site.register(UserOrder)
