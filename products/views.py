from django.shortcuts import render

# Функции = контроллеры = обработчики запросов


def index(request):
    return render(
        request=request,
        template_name='products/index.html',
    )


def products(request):
    return render(
        request=request,
        template_name='products/products.html',
    )
