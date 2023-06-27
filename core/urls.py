from django.urls import path
from .views import home, product, add_to_cart, remove_from_cart, cart

urlpatterns = [
	path("", home, name="home"),
	path("product", product, name="product"),
	path("add_to_cart", add_to_cart, name="add_to_cart"),
	path("remove_from_cart", remove_from_cart, name="remove_from_cart"),
	path("cart", cart, name="cart")
]