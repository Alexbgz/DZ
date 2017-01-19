from django.db import models
from django.contrib.auth.models import User


class Catalog(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    product = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    foto = models.ImageField(blank=True, upload_to='images', verbose_name='Ссылка картинки')

    def image_img(self):
        if self.foto:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.foto.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    iduser = models.ForeignKey(User)
    idproduct = models.ForeignKey(Catalog)
    quantity = models.IntegerField()
    summ = models.IntegerField()
