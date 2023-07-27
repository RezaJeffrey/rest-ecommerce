# Generated by Django 4.0.6 on 2023-07-27 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productpacks', '0001_initial'),
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdiscount',
            name='product_pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_discounts', to='productpacks.productpack'),
        ),
    ]
