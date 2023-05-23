from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField 
from django_resized import ResizedImageField


STATIT_CHOICE=[
    ("ОТ", "Отмененный"),
    ("АК", "Активный"),
    ("ЗП", "Запрошено"),
    ("ПЛ", "Получено"),
]
#категоории продукта
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название категории")
    description = RichTextUploadingField(verbose_name="описание Категории")

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



#атрибуты продукта
class Atribute(models.Model):
    title = models.CharField(max_length=150, verbose_name="Атрибут")
    value = models.CharField(max_length=50, verbose_name="Значение")
    products = models.ForeignKey('Producte',on_delete=models.CASCADE,related_name="prod_atrib",null=True)
    
    def __str__(self) -> str:
            return self.title
    
    class Meta:
        verbose_name = "Атрибут"
        verbose_name_plural = "Атрибуты"



#сам продукт
class Producte(models.Model):
    title =models.CharField(max_length=300, verbose_name="Название Продукта")
    description = models.CharField(max_length=150, verbose_name="описание Продукта")
    content = RichTextUploadingField(verbose_name="содержание продукта")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product", verbose_name="Категория продукта")
    price = models.IntegerField(default=1, verbose_name="Цена продукта")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, verbose_name="Создатель продукта или автор")


    def __str__(self) -> str:
            return self.title
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"



#фотографии продукта
class Photo(models.Model):
    photo = ResizedImageField(upload_to='media/images/', force_format='WEBP', quality=90, verbose_name="Фото продукта")
    product = models.ForeignKey('Producte',on_delete=models.CASCADE, related_name='photos',verbose_name="Продукт")


    def __str__(self) -> str:
        return self.product.title

    class Meta:

        verbose_name = 'Фото продукта'
        verbose_name_plural = 'фотограффии продукта'




class OrderItem(models.Model):
    order = models.ForeignKey('Order',on_delete=models.CASCADE, null=True ,related_name='items', verbose_name="Заказы" )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=User, verbose_name='Клиент')
    product = models.ForeignKey(Producte, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(default=1, verbose_name='Кол-во товаров')
    status = models.CharField(null=True, default='null',max_length=2, choices=STATIT_CHOICE, verbose_name="Статус заказа" )
    
    def __str__(self):
        return f"Кол-во: {self.quantity}, заказ: {self.product.title}, пользователь {self.user}"

    @property
    def get_total_item_price(self):
        return self.quantity * self.product.price
    
    
    class Meta:
        verbose_name = 'Карточка заказа'
        verbose_name_plural = 'Карточка заказов'

    


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=User, verbose_name='Клиент')
    ordered_date = models.DateTimeField(verbose_name='Дата ив время заказа')
    shipping_address = models.CharField(max_length=300, default="Osh", verbose_name='Адрес клиента')
    payment = models.BooleanField(default=False, verbose_name='Оплата')
    

    def __str__(self):
        return f"Заказы клииента |-{self.user.username}-|"
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    @property
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price

        return total    


# Create your models here.
