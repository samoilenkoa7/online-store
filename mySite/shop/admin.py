from django.contrib import admin
from .models import Account, AccountPlatform, UserOrder


class AdminAccountView(admin.ModelAdmin):
    list_display = ('title', 'level', 'outfits', 'gliders_amount', 'acc_price', 'platform')
    list_filter = ['title', 'level', 'outfits']


class AccountPlatformAdmin(admin.ModelAdmin):
    list_display = ('id', "platform_name")
    list_filter = ('platform_name', )


admin.site.register(Account, AdminAccountView)
admin.site.register(UserOrder)
admin.site.register(AccountPlatform, AccountPlatformAdmin)
