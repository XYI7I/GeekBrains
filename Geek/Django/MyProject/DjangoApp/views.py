from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


logger = logging.getLogger(__name__)


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {'client': client})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})


# Аналогичные функции для товаров:

def prouct_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


# Аналогичные функции для заказов:

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('product_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

# def index(request):
#     logger.info('Index page accessed')
#     return HttpResponse("Hello, world!")
# def about(request):
#     try:
#         # some code that might raise an exception
#         result = 1 / 0
#     except Exception as e:
#         logger.exception(f'Error in about page: {e}')
#         return HttpResponse("Oops, something went wrong.")
#     else:
#         logger.debug('About page accessed')
#         return HttpResponse("This is the about page.")
