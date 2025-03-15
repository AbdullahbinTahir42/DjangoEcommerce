from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitems_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total' : 0}
    
    context = {'items' : items,'order' : order}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitems_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total' : 0}
    
    context = {'items' : items,'order' : order}
    return render(request,'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['Action']

    print('Product ID : ' ,productID)
    print('Action : ' ,action)
    
    return JsonResponse("Item was added" ,safe=False)
