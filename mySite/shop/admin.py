from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Account, AccountPlatform, UserOrder


class AdminAccountView(admin.ModelAdmin):
    list_display = ('get_title_image', 'title', 'level', 'outfits', 'gliders_amount', 'acc_price', 'platform', 'views')
    list_filter = ['title', 'level', 'outfits', 'views']
    list_editable = ('platform', 'acc_price')
    fields = (
        'title_image', 'get_title_image', 'image_1', 'image_2', 'image_3', 'title', 'level', 'outfits', 'gliders_amount', 'acc_price', 'platform', 'views')
    readonly_fields = ('get_title_image', 'views')
    save_on_top = True

    def get_title_image(self, obj):
        if obj.title_image:
            return mark_safe(f'<img src="{obj.title_image.url}" width="75">')

    get_title_image.short_description = 'Title image'


class AccountPlatformAdmin(admin.ModelAdmin):
    list_display = ('id', "platform_name")
    list_filter = ('platform_name',)


admin.site.register(Account, AdminAccountView)
admin.site.register(UserOrder)
admin.site.register(AccountPlatform, AccountPlatformAdmin)
