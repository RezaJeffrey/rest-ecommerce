# Generated by Django 4.0.6 on 2022-11-06 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_extrafieldvalue_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shop',
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ManyToManyField(related_name='products', to='products.shop'),
        ),
    ]
