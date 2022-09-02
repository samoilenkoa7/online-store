from django.db import models
from datetime import datetime


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
    title_image = models.ImageField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField(blank=True)
    title = models.CharField(unique=True, max_length=250, verbose_name='Short description')
    level = models.IntegerField()
    full_acces = models.CharField(choices=YES_NO_CHOICES, max_length=250)
    vbucks = models.IntegerField()
    bling_amount = models.IntegerField()
    gliders_amount = models.IntegerField()
    save_world = models.CharField(choices=YES_NO_CHOICES, max_length=250)
    hot_og = models.CharField(max_length=250)
    platform = models.CharField(max_length=250, verbose_name='PC, PS, Xbox...')
    mail = models.CharField(choices=MAIL_CHOICES, max_length=250, verbose_name='Type of email on account')
    outfits = models.IntegerField()
    emotions = models.IntegerField()
    description = models.TextField(verbose_name='Full account description')
    acc_raiting = models.CharField(max_length=20, default='5*')
    acc_price = models.IntegerField(default=10)
    date_post = models.DateField(default=time_now())

    class Meta:
        ordering = ('-outfits',)

    def __str__(self):
        return self.title


class PostsImages(models.Model):
    images = models.ImageField(upload_to='shop/account_images/', blank=True)
    account = models.ForeignKey(Account, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.images)


class UserOrder(models.Model):
    name = models.CharField(max_length=100, verbose_name='Your name')
    email = models.CharField(max_length=100, verbose_name='Your email')
    account_id = models.TextField(max_length=250, verbose_name='Account ID')

    def __str__(self):
        return str(self.account_id)
