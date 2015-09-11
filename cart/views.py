from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request, 'cart/index.html', {'items': request.user.customer.cartitem_set.all()})

@login_required
def remove(request, id):
	item = get_object_or_404(CartItem, pk=id)
	item.delete()
	return render(request, 'cart/index.html', {'items': request.user.customer.cartitem_set.all()})

@login_required
def addToCart(request, id):
	p = get_object_or_404(Product, pk=id)
	try:
		quantityString = request.POST['quantity']
	except (KeyError):
		return HttpResponse("cart failed")
	else:
		q = int(quantityString);
		if request.user.customer.cartitem_set.filter(product=p).first():
			c = request.user.customer.cartitem_set.filter(product=p).first()
			c.quantity += q
			c.save()
		else:
			c = CartItem(quantity=q, customer=request.user.customer)
			c.save()
			c.product.add(p)
		return HttpResponseRedirect(reverse('cart:index'))

@login_required
def update(request, id):
	item = get_object_or_404(CartItem, pk=id, customer=request.user.customer)
	try:
		quantityString = request.POST['quantity']
	except (KeyError):
		return HttpResponse("cart failed")
	else:
		q = int(quantityString)
		item.quantity = q;
		item.save()
		return HttpResponseRedirect(reverse('cart:index'))