# Generated by Django 4.0.6 on 2023-07-23 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discount', '0001_initial'),
        ('productpacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdiscount',
            name='product_pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_discounts', to='productpacks.productpack'),
        ),
    ]