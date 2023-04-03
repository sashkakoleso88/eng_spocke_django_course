from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required

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


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])