from django.urls import path
from .views import home, product, wishlist, add_to_wishlist, remove_from_wishlist, add_to_cart, remove_from_cart, cart

urlpatterns = [
	path("", home, name="home"),
	path("product", product, name="product"),
	path("wishlist", wishlist, name="wishlist"),
	path("add_to_wishlist", add_to_wishlist, name="add_to_wishlist"),
	path("remove_from_wishlist", remove_from_wishlist, name="remove_from_wishlist"),
	path("add_to_cart", add_to_cart, name="add_to_cart"),
	path("remove_from_cart", remove_from_cart, name="remove_from_cart"),
	path("cart", cart, name="cart")
]