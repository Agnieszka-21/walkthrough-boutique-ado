from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QK5u4P3kg08sHJNLPBnUrtXYMgGQKxZ9OpjNORwWUxx8yBr6xcBxkvLwnDiRzMa6ZJziX83LoyqsxNotDeQ4ap800hdPKVAYa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)