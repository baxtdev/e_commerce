from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from .models import*
from django import forms
from .import models
from .models import STATIT_CHOICE

admin.site.site_title= 'Онлайн магазин'
admin.site.site_header= 'Все продукты для вас'


# Register your models here.
class AtributeInlineForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    value = forms.CharField(max_length=50)
    class Meta:
        model = models.Atribute
        fields = ('title','value')


class PhotoInlineForm(forms.ModelForm):
    photo = forms.ImageField()
    class Meta:
        model = models.Photo
        fields = ("photo",)

all_users = User.objects.all()
product = Producte.objects.all()

class OrderItemInlineForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=all_users)
    product = forms.ModelChoiceField(queryset=product)
    quantity =forms.IntegerField()
    status = forms.ChoiceField(choices=STATIT_CHOICE)
    class Meta:
        model = models.OrderItem
        fields = ("user" , "product" ,"quantity")

class AtributeInline(admin.TabularInline):
    model = models.Atribute
    form = AtributeInlineForm
    extra = 3

class PhotoInline(admin.TabularInline):
    model = models.Photo
    form = PhotoInlineForm
    extra = 6

class OrderItemInline(admin.TabularInline):
    model =OrderItem
    form = OrderItemInlineForm
    extra = 0

        

class ProducteAdmin(admin.ModelAdmin):
    inlines=[AtributeInline, PhotoInline ]    
    readonly_fields = ('get_image' ,)
    list_display = ("title", "category", "user","get_image")
    list_display_links = ("title", "category", "user")
    
    @admin.display(description='image')
    def get_image(self, instance):
        return mark_safe(f'<img src="{instance.photo.url}" width="50px" ')




class AtributeAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "products")
    list_display_links = ("title", "value", "products")



class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,]
    # list_display = ("user")
    # list_display_links = ("user","ordered_date","shipping_address","payment")

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity")
    list_display_links = ("user", "product", "quantity")



class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image', )
    list_display = ("product", "photo","get_image")

    @admin.display(description='image')
    def get_image(self, instance):
        return mark_safe(f'<img src="{instance.photo.url}" width="75px" ')



admin.site.register(models.Producte,ProducteAdmin)
admin.site.register(models.Atribute,AtributeAdmin)
admin.site.register(models.Category,)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(Order,OrderAdmin )
admin.site.register(OrderItem, OrderItemAdmin)



