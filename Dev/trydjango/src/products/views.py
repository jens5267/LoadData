from django.shortcuts import render

from .forms import ProductForm
from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

# def load_detail_view(request):
#     # obj = Load.objects.get(id=2)
#     context = {
#         # 'object': obj
#     }
#     return render(request, 'products/load_detail.html', context)