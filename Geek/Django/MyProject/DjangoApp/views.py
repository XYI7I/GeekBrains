from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Client, Product, Order
# from .forms import ClientForm, ProductForm, OrderForm
#
# def client_list(request):
#     clients = Client.objects.all()
#     return render(request, 'client_list.html', {'clients': clients})
#
# def client_detail(request, pk):
#     client = get_object_or_404(Client, pk=pk)
#     return render(request, 'client_detail.html', {'client': client})
#
# def client_create(request):
#     if request.method == 'POST':
#         form = ClientForm(request.POST)
#         if form.is_valid():
#             client = form.save()
#             return redirect('client_detail', pk=client.pk)
#     else:
#         form = ClientForm()
#     return render(request, 'client_form.html', {'form': form})

# Аналогичные функции для товаров и заказов...
def index(request):
    return HttpResponse("Hello, world!")
def about(request):
    return HttpResponse("About us")