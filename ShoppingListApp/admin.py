from django.contrib import admin
from .models import shoppingListModel

admin.site.register(shoppingListModel.ShoppingList)
