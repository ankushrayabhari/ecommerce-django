from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
	return render(request, 'main/index.html', {"products": Product.objects.all()})