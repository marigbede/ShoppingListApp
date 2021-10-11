from enum import IntEnum

from ShoppingListApp.utility import TextProcessors


class ShoppingListItemStatus(IntEnum):
    """ Int based enum for shopping list items status """
    Pending = 0
    InCart = 1
    NotAvailable = 2
    BuyLater = 3
    TooExpensive = 4
    Bought = 5

    @classmethod
    def choices(cls):
        """ returns a tuple for find and retrieve operations """
        return [(key.value, key.name) for key in cls]

    @classmethod
    def dictionary(cls):
        """ convert the enum to a JSON based array """
        return [{"keyName": TextProcessors.split_title_case(key.name), "keyValue": key.value} for key in cls]
