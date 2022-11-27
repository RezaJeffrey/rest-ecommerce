# Generated by Django 4.0.6 on 2022-11-08 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productpacks', '0004_alter_productpack_extra_field_values'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0003_alter_pack_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('sku', models.CharField(blank=True, max_length=255, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('sku', models.CharField(blank=True, max_length=255, unique=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='carts.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='productpacks.productpack')),
            ],
            options={
                'unique_together': {('cart', 'item')},
            },
        ),
    ]