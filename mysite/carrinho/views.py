from django.shortcuts import render
from .models import Brand
from django.http import HttpResponse


def index(request):
    brand_list = Brand.objects.order_by('-foundation_Date')[:5]
    context = {'brand_list': brand_list}
    return render(request, 'index.html', context)

def detail_brand(request, brand_id):
    brand = Brand.objects.get(id = brand_id)
    return render(request, 'detail.html', {'brand': brand})