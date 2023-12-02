from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create(quantity_from_form,total_charge):
        return Order.objects.create(
            quantity_ordered=quantity_from_form,
            total_price=total_charge
            )

    def show(id):
        return Order.objects.get(id=int(id))

    def all():
        all_orders = Order.objects.all()
        x = 0
        y = 0
        for order in all_orders:
            x += order.quantity_ordered
            y += order.total_price
        return (x,y)