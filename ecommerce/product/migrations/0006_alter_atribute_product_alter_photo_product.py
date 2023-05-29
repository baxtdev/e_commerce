# Generated by Django 4.2 on 2023-05-29 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_producte_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atribute',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atributes', to='product.producte'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='product.producte', verbose_name='Продукт'),
        ),
    ]