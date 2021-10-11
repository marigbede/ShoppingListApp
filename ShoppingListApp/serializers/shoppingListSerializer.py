from rest_framework import serializers

from ShoppingListApp.models.shoppingListModel import ShoppingList


class GetShoppingListSerializer(serializers.ModelSerializer):
    itemStatusText = serializers.CharField(source='get_shopping_list_item_type_text')

    class Meta:
        model = ShoppingList
        fields = ('id', 'itemName', 'itemStatus', 'itemStatusText', 'marketAmount', 'marketAmountDate')


class PostShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('itemName', 'itemStatus', 'marketAmount', 'marketAmountDate')


class DeleteShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('id',)
