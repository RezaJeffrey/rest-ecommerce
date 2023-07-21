from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=200, unique=True, blank=False, null=True)
    image = models.ImageField(upload_to='images/category/', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='child', blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ('name',)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
