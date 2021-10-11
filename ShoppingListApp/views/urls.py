from django.urls import path
from . import shoppingListAppClient

urlpatterns = [
    path('', shoppingListAppClient.index, name="index")
]