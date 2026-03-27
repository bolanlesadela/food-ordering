from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Order

def menu(request):
    items = MenuItem.objects.filter(available=True)
    return render(request, 'menu/menu.html', {'items': items})

def place_order(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        quantity = int(request.POST.get('quantity', 1))
        Order.objects.create(customer_name=customer_name, item=item, quantity=quantity)
        return redirect('orders')
    return render(request, 'menu/order.html', {'item': item})

def orders(request):
    all_orders = Order.objects.all().order_by('-created_at')
    return render(request, 'menu/orders.html', {'orders': all_orders})

def update_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.status == 'pending':
        order.status = 'confirmed'
    elif order.status == 'confirmed':
        order.status = 'delivered'
    order.save()
    return redirect('orders')