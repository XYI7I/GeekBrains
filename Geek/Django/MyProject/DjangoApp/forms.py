# forms.py

from django import forms
from .models import User, Product, Order


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'address']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['order_date']
        fields = ['user', 'products', 'total_amount']
