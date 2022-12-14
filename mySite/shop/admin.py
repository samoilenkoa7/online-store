from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Account, AccountPlatform, UserOrder, AccountPics
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ImageInline(admin.TabularInline):
     model = AccountPics

class AccountAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Account
        fields = '__all__'


class AdminAccountView(admin.ModelAdmin):
    form = AccountAdminForm
    inlines = [ImageInline]
    list_display = ('get_title_image', 'title', 'level', 'outfits', 'gliders_amount', 'acc_price', 'platform', 'views')
    list_filter = ['title', 'level', 'outfits', 'views']
    list_editable = ('platform', 'acc_price')
    fields = (
        'title_image', 'get_title_image', 'title', 'description', 'mail', 'hot_og',
        'outfits', 'emotions', 'level', 'vbucks', 'gliders_amount', 'bling_amount', 'acc_price',
        'acc_raiting', 'platform', 'views', 'full_acces')
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
