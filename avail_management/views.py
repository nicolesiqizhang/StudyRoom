from django.shortcuts import render
from polls.algorithm.finder import load_active_orders
from polls.algorithm.finder import find_next_available
from polls.forms import NewOrderForm
from polls.models import Order


# Create your views here.
def list_order(request):
    if request.method == 'POST':
        new_order_form = NewOrderForm(request.POST)

        if new_order_form.is_valid():
            new_order = Order()
            new_order.start_date = new_order_form.cleaned_data['start_date']
            new_order.end_date = new_order_form.cleaned_data['end_date']
            new_order.customer_name = new_order_form.cleaned_data['customer_name']
            new_order.staff_name = new_order_form.cleaned_data['staff_name']
            new_order.save()

    else:
        new_order_form = NewOrderForm(initial={'start_date': datetime.date.today()})

    order_list = load_active_orders()
    max_capacity = 14
    next_avail_date = find_next_available(max_capacity, order_list)
    allow_new_customer = datetime.datetime.today().date() >= next_avail_date.date()

    context = {
        'order_list': order_list,
        'max_capacity': max_capacity,
        'next_avail_date': next_avail_date,
        'new_order_form': new_order_form,
        'allow_new_customer': allow_new_customer
    }
    return render(request, "avail_management/orders.html", context)