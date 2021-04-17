from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    template_name = 'cart/product_list_html'
    queryset = Product.objects.all()
