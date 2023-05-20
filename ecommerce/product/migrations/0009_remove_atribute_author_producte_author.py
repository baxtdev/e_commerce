# Generated by Django 4.2 on 2023-04-27 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0008_atribute_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atribute',
            name='author',
        ),
        migrations.AddField(
            model_name='producte',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
