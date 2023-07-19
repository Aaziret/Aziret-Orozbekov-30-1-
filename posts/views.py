from django.shortcuts import render
from posts.models import Product


def main_view(requests):
    if requests.method == 'GET':
        return render(requests, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/product.html', context=context)
