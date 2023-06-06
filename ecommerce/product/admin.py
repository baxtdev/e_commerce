from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from .models import*
from django import forms
from .import models
from .models import STATIT_CHOICE



admin.site.site_title= 'Онлайн магазин'
admin.site.site_header= 'Все продукты для вас'



#forms
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



class OrderItemInlineForm(forms.ModelForm):
    products = Producte.objects.all()
    #form для ordera
    product = forms.ModelChoiceField(queryset=products)
    quantity =forms.IntegerField(initial=1)
    status = forms.ChoiceField(choices=STATIT_CHOICE)
    class Meta:
        model = models.OrderItem
        fields = ( "product" ,"quantity","status")

#inlines
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
    list_display = ("title", "category", "user","created_date")#"photo","get_image"
    list_display_links = ("title", "category", "user",)#"photo"
    
    @admin.display(description='image')
    def get_image(self, instance):
        return mark_safe(f'<img src="{instance.photo.photo.url}" width="50px" ')



class AtributeAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "product")
    list_display_links = ("title", "value", "product")



class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,]
    list_display = ("user","shipping_address","payment","ordered_date","get_total"  )
    list_display_links = ("user","shipping_address")



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity","get_total_item_price")
    list_display_links = ("order", "product", "quantity")



class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image', )
    list_display = ("product", "photo","get_image")

    @admin.display(description='image')
    def get_image(self, instance):
        return mark_safe(f'<img src="{instance.photo.url}" width="75px" ')



admin.site.register(models.Producte,ProducteAdmin)
admin.site.register(models.Atribute,AtributeAdmin)
admin.site.register(models.Category)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(Order,OrderAdmin )
admin.site.register(OrderItem, OrderItemAdmin)



