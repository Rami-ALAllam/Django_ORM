from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    pre = Product.objects.get(id=1)
    request.session['id'] = pre.id
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product_ordered = Product.objects.get(id=request.POST["product_id"])
    price_from_form = float(product_ordered.price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card..."+str(total_charge))
    X = Order.create(
        quantity_from_form,
        total_charge
    )
    return redirect("/Bill/"+str(X.id))

def Bill(request,id):
    context={
        "order": Order.show(id),
        "allorders":Order.all(),
    }
    return render(request, "store/checkout.html",context)
