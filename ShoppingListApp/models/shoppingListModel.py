from django.db import models

from ShoppingListApp.enums.shoppingListItemStatus import ShoppingListItemStatus
from ShoppingListApp.utility import TextProcessors


class ShoppingList(models.Model):
    class Meta:
        verbose_name = "Shopping List"
        verbose_name_plural = "Shopping Lists"

    itemName = models.CharField(blank=False, max_length=20)
    itemStatus = models.IntegerField(choices=ShoppingListItemStatus.choices(),
                                     default=ShoppingListItemStatus.Pending)
    marketAmount = models.FloatField(default=0, blank=True, null=True)
    marketAmountDate = models.DateTimeField(default=None, blank=True, null=True)

    @property
    def get_shopping_list_item_type_text(self):
        return TextProcessors.split_title_case(ShoppingListItemStatus(self.itemStatus).name)

    def __str__(self):
        return self.itemName
