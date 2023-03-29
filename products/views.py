from django.shortcuts import render
from products.models import Product, ProductCategory

# Функции = контроллеры = обработчики запросов


def index(request):
    context = {
        'title': 'Store',
    }
    return render(
        request=request,
        template_name='products/index.html',
        context=context,
    )


def products(request):
    context = {
        'title': 'Store - catalog',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(
        request=request,
        template_name='products/products.html',
        context=context,
    )
