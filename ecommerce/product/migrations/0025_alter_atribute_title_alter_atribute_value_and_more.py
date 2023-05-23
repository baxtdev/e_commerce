# Generated by Django 4.2 on 2023-05-23 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0024_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atribute',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Атрибут'),
        ),
        migrations.AlterField(
            model_name='atribute',
            name='value',
            field=models.CharField(max_length=50, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='product.order', verbose_name='Заказы'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('ОТ', 'Отмененный'), ('АК', 'Активный'), ('ЗП', 'Запрошено'), ('ПЛ', 'Получено')], default='null', max_length=2, null=True, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=90, scale=None, size=[1920, 1080], upload_to='media/images/', verbose_name='Фото продукта'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='product.producte', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='producte',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель продукта или автор'),
        ),
        migrations.AlterField(
            model_name='producte',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.category', verbose_name='Категория продукта'),
        ),
        migrations.AlterField(
            model_name='producte',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Цена продукта'),
        ),
        migrations.AlterField(
            model_name='producte',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Название Продукта'),
        ),
    ]
