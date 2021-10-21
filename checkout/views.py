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
        'stripe_public_key': (
            'pk_test_51JlvmQKSXYN6Aotn8KJf1ChFTzhXd3yJD6ENOx59a7n3fgGkq82RlEKryZfxk5v7AcDKGphDOQmRLiJehoa2KxhZ00tYoKbXsz'),
        'client_secret': (
            'sk_test_51JlvmQKSXYN6AotnBrjFUYh1izmXd3ExtiTpEWxlzIp6UM8sDVJLQWxdsp64B4EIi0g0vXCGC65VU4ftGcg31a1I00nlV9vPZ6'),
    }

    return render(request, template, context)
