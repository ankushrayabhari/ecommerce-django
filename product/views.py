from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from cart.models import *

# Create your views here.
def index(request):
	list = get_list_or_404(Product.objects.all())
	return render(request, 'product/index.html', {'products': list})

def detail(request, id):
	product = get_object_or_404(Product, pk=id)
	return render(request, 'product/detail.html', {'product': product})

def related(request, id):
	product = get_object_or_404(Product, pk=id)
	return render(request, 'product/related.html', {'product': product})