from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy


def time_now():
    return datetime.now()


class Account(models.Model):
    YES_NO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    MAIL_CHOICES = (
        ('Connected', 'Email in pack'),
        ('No email', 'No email'),
        ('Others', 'Other')
    )
    title_image = models.ImageField(upload_to='shop/account_images/%Y/%m/%d', blank=True)
    title = models.CharField(unique=True, max_length=250, verbose_name='Short description')
    level = models.IntegerField()
    full_acces = models.CharField(choices=YES_NO_CHOICES, max_length=250)
    vbucks = models.IntegerField()
    bling_amount = models.IntegerField()
    gliders_amount = models.IntegerField()
    save_world = models.CharField(choices=YES_NO_CHOICES, max_length=250)
    hot_og = models.CharField(max_length=250)
    platform = models.ForeignKey('AccountPlatform', on_delete=models.CASCADE)
    mail = models.CharField(choices=MAIL_CHOICES, max_length=250, verbose_name='Type of email on account')
    outfits = models.IntegerField()
    emotions = models.IntegerField()
    description = models.TextField(verbose_name='Full account description')
    acc_raiting = models.CharField(max_length=20, default='5*')
    acc_price = models.IntegerField(default=10)
    date_post = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def is_new(self):
        return self.date_post >= (timezone.now() - timedelta(days=7))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('order', kwargs={'account_id': self.pk})

    class Meta:
        ordering = ('-outfits',)


class AccountPics(models.Model):
    image_1 = models.ImageField(upload_to='shop/account_images/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='shop/account_images/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(blank=True)
    acc = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'Pictures for account {self.acc}'


class AccountPlatform(models.Model):
    platform_name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.platform_name

    def get_absolute_url(self):
        return reverse_lazy('platform', kwargs={'accountplatform_id': self.pk})


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account_id = models.TextField(max_length=250, verbose_name='Account ID')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account_id)
