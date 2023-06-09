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



#сам продукт
class Producte(models.Model):
    title =models.CharField(max_length=300, verbose_name="Название Продукта")
    description = models.CharField(max_length=150, verbose_name="описание Продукта")
    content = RichTextUploadingField(verbose_name="содержание продукта",null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products", verbose_name="Категория продукта")
    price = models.IntegerField(default=1, verbose_name="Цена продукта")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, verbose_name="Создатель продукта или автор")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата созздание продукта")
    def __str__(self) -> str:
            return self.title
    
    @property
    def photo(self):
        return self.photos.first()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"



#атрибуты продукта
class Atribute(models.Model):
    title = models.CharField(max_length=150, verbose_name="Атрибут")
    value = models.CharField(max_length=200, verbose_name="Значение")
    product = models.ForeignKey('Producte',on_delete=models.CASCADE,related_name="atributes",null=True)
    
    def __str__(self) -> str:
            return self.title
    
    class Meta:
        verbose_name = "Атрибут"
        verbose_name_plural = "Атрибуты"



#фотографии продукта
class Photo(models.Model):
    photo = ResizedImageField(upload_to='media/images/', force_format='WEBP', quality=90, verbose_name="Фото продукта")
    product = models.ForeignKey('Producte',on_delete=models.CASCADE, related_name='photos',verbose_name="Продукт")

    def __str__(self) -> str:
        return self.photo.url

    class Meta:

        verbose_name = 'Фото продукта'
        verbose_name_plural = 'фотограффии продукта'



#карточки заказ
class OrderItem(models.Model):
    order = models.ForeignKey('Order',on_delete=models.CASCADE, null=True ,related_name='items', verbose_name="Заказы")
    product = models.ForeignKey(Producte, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(default=1, verbose_name='Кол-во товаров', null=False)
    status = models.CharField(null=True, default='АК',max_length=10, choices=STATIT_CHOICE, verbose_name="Статус заказа" )
    
    def __str__(self):
        return f"Кол-во: {self.quantity}, заказ: {self.product.title}, пользователь {self.order.user.username}"

    @property
    def get_total_item_price(self):
        return self.quantity * self.product.price
    
    class Meta:
        verbose_name = 'Карточка заказа'
        verbose_name_plural = 'Карточка заказов'

    

#заказы
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=User, verbose_name='Клиент')
    ordered_date = models.DateTimeField(verbose_name='Дата ив время заказа',auto_now_add=True)
    shipping_address = models.CharField(max_length=300, verbose_name='Адрес клиента', null=False)
    payment = models.BooleanField(default=True, verbose_name='Оплата')
    

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
