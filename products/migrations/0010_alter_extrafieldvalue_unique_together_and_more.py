# Generated by Django 4.0.6 on 2022-11-05 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productpacks', '0004_alter_productpack_extra_field_values'),
        ('products', '0009_alter_extrafieldvalue_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='extrafieldvalue',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='extrafieldvalue',
            name='field_name',
        ),
        migrations.RemoveField(
            model_name='extrafieldvalue',
            name='product',
        ),
        migrations.DeleteModel(
            name='ExtraFieldName',
        ),
        migrations.DeleteModel(
            name='ExtraFieldValue',
        ),
    ]
