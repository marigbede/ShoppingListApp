from rest_framework.decorators import api_view

from ShoppingListApp.logic.shoppingListLogic import ShoppingListLogic


@api_view(('GET',))
def get_shopping_list(request):
    return ShoppingListLogic.get_shopping_list_items(request)


@api_view(('GET',))
def get_shopping_list_item(request, item_id):
    return ShoppingListLogic.get_shopping_list_item(request, item_id)


@api_view(('GET',))
def get_shopping_list_status_options(request):
    return ShoppingListLogic.get_shopping_list_status_options(request)


@api_view(('POST',))
def post_shopping_list(request):
    return ShoppingListLogic.post_shopping_list_item(request)


@api_view(('POST',))
def clear_shopping_list(request):
    return ShoppingListLogic.clear_shopping_list(request)


@api_view(('POST',))
def delete_shopping_list(request):
    return ShoppingListLogic.delete_shopping_list_item(request)
