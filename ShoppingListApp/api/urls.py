from django.urls import path

from .shoppingListApi import *

urlpatterns = [
    path('getshoppinglist/', get_shopping_list, name='api-get-shopping-list'),
    path('getshoppinglistitem/<int:item_id>', get_shopping_list_item, name='api-get-shopping-list-item'),
    path('getshoppingliststatusoptions/', get_shopping_list_status_options,
         name='api-get-shopping-list-status-options'),
    path('postshoppinglist/', post_shopping_list, name='api-post-shopping-list'),
    path('clearshoppinglist/', clear_shopping_list, name='api-clear-shopping-list'),
    path('deleteshoppinglist/', delete_shopping_list, name='api-delete-shopping-list')
]
