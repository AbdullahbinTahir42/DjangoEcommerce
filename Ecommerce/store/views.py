from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitems_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total' : 0}
        cart_items = order['get_cart_items']
    products = Product.objects.all()
    context = {"products" : products,'cart_items':cart_items}
    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitems_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total' : 0}
        cart_items = order['get_cart_items']
    
    context = {'items' : items,'order' : order,'cart_items':cart_items}
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

    print('Product ID:', productID)
    print('Action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItems.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity += 1
    elif action == 'remove':     
        orderitem.quantity -= 1 

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse({"success": True}) 