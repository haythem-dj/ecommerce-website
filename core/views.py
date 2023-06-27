from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from users.models import Profile

def home(request):
	context = {
		"products": Product.objects.all()
	}

	return render(request, "core/home.html", context=context)

@login_required(login_url="RegisterLogin")
def product(request):
	context = {}

	id = request.GET.get("id", None)
	if not id.isnumeric():
		return redirect("home")

	id = int(id)
		
	product = Product.objects.filter(id=id).first()

	if not product:
		return redirect("home")

	context = {
		"product": Product.objects.filter(id=id).first()
	}

	return render(request, "core/product.html", context=context)

@login_required(login_url="RegisterLogin")
def add_to_cart(request):
	id = request.GET.get("id", None)

	if not id.isnumeric():
		return redirect("home")

	id = int(id)

	profile = Profile.objects.filter(user=request.user).first()
	product = Product.objects.filter(id=id).first()

	if not product:
		return redirect("home")

	if Order.objects.filter(profile=profile).exists():
		Order.objects.filter(profile=profile).first().products.add(product)
		print("hi")
	else:
		order = Order(profile=profile)
		order.save()
		order.products.add(product)

	return redirect("home")

@login_required(login_url="RegisterLogin")
def remove_from_cart(request):
	id = request.GET.get("id", None)

	if not id.isnumeric():
		return redirect("home")

	id = int(id)
	profile = Profile.objects.filter(user=request.user).first()
	order = Order.objects.filter(profile=profile).first()
	product = Product.objects.filter(id=id).first()

	if not order:
		return redirect("home")

	if product not in Order.objects.filter(profile=profile).first().products.all():
		return redirect("home")

	order.products.remove(product)
	return redirect("cart")

@login_required(login_url="RegisterLogin")
def cart(request):
	profile = Profile.objects.filter(user=request.user).first()
	order = Order.objects.filter(profile=profile).first()

	if not order:
		return render(request, "core/cart.html")

	products = order.products.all()

	context = {
		"products": products
	}

	return render(request, "core/cart.html", context=context)