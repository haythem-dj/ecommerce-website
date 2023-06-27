from django.urls import path
from .views import RegisterLoginView, logoutView

urlpatterns = [
	path("login/", RegisterLoginView, name="RegisterLogin"),
	path("logout/", logoutView, name="logout")
]