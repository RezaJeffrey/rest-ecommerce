# Generated by Django 4.0.6 on 2022-10-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_extrafieldvalue_field_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrafieldvalue',
            name='sku',
            field=models.CharField(max_length=255, null=True),
        ),
    ]