from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ShoppingListApp.models.shoppingListModel import ShoppingList
from ShoppingListApp.enums.shoppingListItemStatus import ShoppingListItemStatus


class ShoppingListApis(APITestCase):
    def test_get_shopping_list_items(self):
        response = self.client.get(reverse('api-get-shopping-list'), format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_shopping_list_item(self):
        response = self.client.get(f"{reverse('api-get-shopping-list-item', args={0})}", format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_shopping_list_item(self):
        self.assertEquals(
            ShoppingList.objects.count(),
            0
        )

        data = {
            'itemName': 'Item 1',
            'itemStatus': ShoppingListItemStatus.Pending
        }

        response = self.client.post(reverse('api-post-shopping-list'), data=data, format='json')

        self.assertEquals(
            ShoppingList.objects.count(),
            1
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_shopping_list_item(self):
        data = {
            'itemName': 'Item 1',
            'itemStatus': ShoppingListItemStatus.Pending
        }
        self.client.post(reverse('api-post-shopping-list'), data=data, format='json')

        data = {
            'id': 1
        }
        response = self.client.post(reverse('api-delete-shopping-list'), data=data, format='json')

        self.assertEquals(
            ShoppingList.objects.count(),
            0
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_clear_shopping_list_item(self):
        data = {
            'itemName': 'Item 1',
            'itemStatus': ShoppingListItemStatus.Pending
        }
        self.client.post(reverse('api-post-shopping-list'), data=data, format='json')

        response = self.client.post(reverse('api-clear-shopping-list'), format='json')

        self.assertEquals(
            ShoppingList.objects.count(),
            0
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)
