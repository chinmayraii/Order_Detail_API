from django.shortcuts import render
from . models import Order,OrderDetails
import uuid

def index(request):
    order_data=Order.objects.all()
    return render (request,'home.html',{'order_data':order_data})


def add_order(request):
    order_category=request.POST['order_category']
    order_name=request.POST['order_name']
    order_quantity=request.POST['order_quantity']
    Order.objects.create(order_category=order_category,order_quantity=order_quantity, order_name=order_name)
    order_data=Order.objects.all()
    return render (request,'home.html',{'order_data':order_data})





