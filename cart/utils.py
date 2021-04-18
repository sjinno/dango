import .models import Order


def get_or_set_order_session(request):
    order_id = request.session.get('order_id', None)
    if order_id is None:
        order = Order()
        order.save()
        request.session('order_id') = order_id
    else:
