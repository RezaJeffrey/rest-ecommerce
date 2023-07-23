from django.db import models
from datetimemixin.models import DateTimeMixin
from productpacks.models import ProductPack
from blacklists.models import Blacklist


 # discount on single products using code/ discount by price
class DiscountCode(DateTimeMixin):
     code = models.CharField(max_length=30)
     available_untill = models.DateTimeField()


class ProductDiscount(DateTimeMixin):
     product_pack = models.ForeignKey(ProductPack, on_delete=models.CASCADE, related_name="product_discounts")
     discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, related_name="product_discounts")
     new_price = models.DecimalField(decimal_places=2, max_digits=14)
     percent = models.PositiveIntegerField(default=0)
     black_list = models.ForeignKey(
         to=Blacklist,
         on_delete=models.DO_NOTHING,
         blank=True,
         null=True,
         related_name="codes"
     )

     def __str__(self):
         return f'{self.product.name} -p {self.percent}%'