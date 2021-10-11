from rest_framework.decorators import api_view

from ShoppingListApp.logic.shoppingListLogic import ShoppingListLogic


@api_view(('GET',))
def get_shopping_list(request):
    """ Get all items from the database """
    return ShoppingListLogic.get_shopping_list_items(request)


@api_view(('GET',))
def get_shopping_list_item(request, item_id):
    """ Get a single shopping list item from the database """
    return ShoppingListLogic.get_shopping_list_item(request, item_id)


@api_view(('GET',))
def get_shopping_list_status_options(request):
    """ Gets a list of shopping list status options for the front end """
    return ShoppingListLogic.get_shopping_list_status_options(request)


@api_view(('POST',))
def post_shopping_list(request):
    """ Save a single shopping list item to the database """
    return ShoppingListLogic.post_shopping_list_item(request)


@api_view(('POST',))
def clear_shopping_list(request):
    """ Clear the entire database of all saved shopping items """
    return ShoppingListLogic.clear_shopping_list(request)


@api_view(('POST',))
def delete_shopping_list(request):
    """ Delete a single shopping item from the database """
    return ShoppingListLogic.delete_shopping_list_item(request)
