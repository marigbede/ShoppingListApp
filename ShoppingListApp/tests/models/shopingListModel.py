from django.test import TestCase

from ShoppingListApp.enums.shoppingListItemStatus import ShoppingListItemStatus
from ShoppingListApp.models.shoppingListModel import ShoppingList


class ShoppingListModelTestCase(TestCase):
    def test_create(self):
        self.assertEquals(
            ShoppingList.objects.count(),
            0
        )

        ShoppingList.objects.create(
            itemName="Item 1", itemStatus=ShoppingListItemStatus.Pending
        )

        self.assertEquals(
            ShoppingList.objects.count(),
            1
        )

    def test_read(self):
        ShoppingList.objects.create(
            itemName="Item 1", itemStatus=ShoppingListItemStatus.Pending
        )

        shopping_list_item = ShoppingList.objects.filter(itemName='Item 1').first()

        self.assertEquals(
            shopping_list_item.itemName,
            "Item 1"
        )

    def test_update(self):
        ShoppingList.objects.create(
            itemName="Item 1", itemStatus=ShoppingListItemStatus.Pending
        )

        shopping_list_item = ShoppingList.objects.filter(itemName='Item 1').first()

        shopping_list_item.itemName = 'Item 2'
        shopping_list_item.save()

        shopping_list_item = ShoppingList.objects.filter(itemName='Item 2').first()

        self.assertEquals(
            shopping_list_item.itemName,
            "Item 2"
        )

    def test_delete(self):
        ShoppingList.objects.create(
            itemName="Item 1", itemStatus=ShoppingListItemStatus.Pending
        )

        shopping_list_item = ShoppingList.objects.filter(itemName='Item 1').first()

        ShoppingList.delete(shopping_list_item)

        self.assertEquals(
            ShoppingList.objects.count(),
            0
        )
