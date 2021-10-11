from django.shortcuts import render


def index(request):
    return render(request, 'ShoppingListApp/index.html')
