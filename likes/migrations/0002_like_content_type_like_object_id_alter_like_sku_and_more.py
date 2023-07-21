# Generated by Django 4.0.6 on 2023-07-19 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='like',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like',
            name='sku',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'object_id')},
        ),
        migrations.AddIndex(
            model_name='like',
            index=models.Index(fields=['content_type', 'object_id'], name='likes_like_content_5c134b_idx'),
        ),
    ]
