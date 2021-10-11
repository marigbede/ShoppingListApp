from ShoppingListApp.serializers.shoppingListSerializer import *
from ShoppingListApp.models.shoppingListModel import ShoppingList
from ShoppingListApp.enums.shoppingListItemStatus import ShoppingListItemStatus
from ShoppingListApp.utility import ResponseProcessors


class ShoppingListLogic:
    def get_shopping_list_items(self):
        return ResponseProcessors\
            .success(GetShoppingListSerializer(ShoppingList.objects.all().order_by('itemName'), many=True).data)

    def get_shopping_list_item(self, item_id):
        if ShoppingList.objects.filter(pk=item_id).exists():
            return ResponseProcessors.success(GetShoppingListSerializer(ShoppingList.objects.get(pk=item_id),
                                                                        many=False).data)
        else:
            return ResponseProcessors.failed(f'Cannot find item of Id: {item_id}')

    def post_shopping_list_item(self):
        if self.data is None:
            ResponseProcessors.failed('The Payload is Empty')

        post_serialize = PostShoppingListSerializer(data=self.data)

        if not post_serialize.is_valid():
            return ResponseProcessors.failed('The Payload is Invalid')

        item_name = str(self.data["itemName"]).strip()

        item_id = int(self.data.get("id", 0))

        if item_id == 0:
            if ShoppingList.objects.filter(itemName__iexact=item_name):
                return ResponseProcessors.failed(f'Item {item_name} has already been added')

            post_serialize.save()
        else:
            existing_item = ShoppingList.objects.get(pk=item_id)
            existing_item.itemName = item_name
            existing_item.itemStatus = int(self.data["itemStatus"])
            existing_item.marketAmount = float(self.data.get("marketAmount", 0))

            existing_item.save()

        return ResponseProcessors.success()

    def delete_shopping_list_item(self):
        if self.data is None:
            ResponseProcessors.failed('The Payload is Empty')

        delete_serialize = DeleteShoppingListSerializer(data=self.data)

        if not delete_serialize.is_valid():
            return ResponseProcessors.failed('The Payload is Invalid')

        if not ShoppingList.objects.filter(id=self.data["id"]):
            return ResponseProcessors.failed('That Shopping Item does not exist')

        ShoppingList.delete(ShoppingList.objects.filter(id=self.data["id"]).first())
        return ResponseProcessors.success()

    def get_shopping_list_status_options(self):
        return ResponseProcessors.success(ShoppingListItemStatus.dictionary())

    def clear_shopping_list(self):
        ShoppingList.objects.all().delete()
        return ResponseProcessors.success()
