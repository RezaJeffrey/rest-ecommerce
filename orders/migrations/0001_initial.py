# Generated by Django 4.0.6 on 2023-07-27 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(choices=[('cd', 'cash on delivery'), ('nb', 'net banking'), ('cp', 'card payment'), ('wl', 'wallet')], default='cd', max_length=2, verbose_name='payment method')),
                ('sku', models.CharField(blank=True, max_length=255, unique=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='address.address')),
                ('order_cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='carts.cart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pn', 'order pending'), ('oa', 'order approved'), ('sp', 'order shipped'), ('od', 'order delivered'), ('oc', 'order cancelled'), ('or', 'order returned')], default='pn', max_length=2)),
                ('sku', models.CharField(blank=True, max_length=255, unique=True)),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
