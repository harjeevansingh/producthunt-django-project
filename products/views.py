from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


def sell(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['title'] and request.POST['body'] and request.POST['price'] and request.POST['location'] and request.FILES['image']:
                product = Product()
                product.title = request.POST['title']
                product.price = request.POST['price']
                product.body = request.POST['body']
                product.location = request.POST['location']
                product.image = request.FILES['image']
                product.pub_date = timezone.datetime.now()
                product.hunter = request.user
                product.save()
                return redirect('/products/' + str(product.id))

            else:
                return render(request, 'products/sell.html', {'error': "All fields are required!"})

        return render(request, 'products/sell.html')

    else:
        return render(request, 'accounts/login.html', {'error': "You must login first!"})
