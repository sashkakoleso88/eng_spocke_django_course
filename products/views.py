from django.shortcuts import render

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
        'products': [
            {
                'image': "/static/vendor/img/products/Adidas-hoodie.png",
                'name': "Худи черного цвета с монограммами adidas Originals",
                'price': 6090,
                'description': "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
            },
            {
                'image': "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
                'name': "Синяя куртка The North Face",
                'price': 23725,
                'description': "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
            },
            {
                'image': "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
                'name': "Коричневый спортивный oversized-топ ASOS DESIGN",
                'price': 3390,
                'description': "Материал с плюшевой текстурой. Удобный и мягкий.",
            },
        ]
    }
    return render(
        request=request,
        template_name='products/products.html',
        context=context,
    )
