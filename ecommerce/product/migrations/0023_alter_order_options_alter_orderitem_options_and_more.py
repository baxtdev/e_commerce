# Generated by Django 4.2 on 2023-05-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_remove_order_items_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Карточка заказа', 'verbose_name_plural': 'Карточка заказов'},
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('ОТ', 'Отмененный'), ('АК', 'Активный'), ('ЗП', 'Запрошено'), ('ПЛ', 'Получено')], default='ОТ', max_length=2),
        ),
    ]