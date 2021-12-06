from django.shortcuts import get_object_or_404, render
from .models import Product
from cart.models import CartItem
from django.core.paginator import Paginator



def product_list(request):
  queryset = Product.objects.filter(featured = True)
  paginator = Paginator(queryset, 3)
  page = request.GET.get('page')
  paged_products = paginator.get_page(page)
  context = {
    "products": paged_products
  }
  return render(request, "products/products.html", context)

def single_product(request, id):
  product = get_object_or_404(Product, id = id)
  in_cart = False
  if CartItem.objects.filter(product = product, user = request.user).exists():
    in_cart = True
  context = {
    "product": product,
    "in_cart": in_cart
  }
  return render(request, "products/single-product.html", context)