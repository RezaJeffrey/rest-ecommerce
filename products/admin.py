from django.contrib import admin
from products import models


admin.site.register(models.Shop)
admin.site.register(models.Brand)
admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.Commment)

