from django.shortcuts import render, redirect
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from core.models import WishList

def RegisterLoginView(request):
	if request.user.is_authenticated:
		return redirect("home")
		
	if request.method == 'POST':
		typ = request.POST["type"]
		if typ == "login":
			email = request.POST["email"]
			password = request.POST["password"]

			if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
				if "@" in email:
					user = User.objects.filter(email=email).first()
				else: user = User.objects.filter(username=email).first()

				if not user.check_password(password):
					return render(request, "users/register_login.html", context={"error": "the password is incorrect"})

				auth_login(request, user)
				return redirect("home")

			return render(request, "users/register_login.html", context={"error": "this account does not exist"})

		elif typ == "register":
			email = request.POST["email"]
			username = request.POST["username"]
			firstname = request.POST["firstname"]
			lastname = request.POST["lastname"]
			password = request.POST["password"]
			password2 = request.POST["password2"]

			if User.objects.filter(email=email).exists():
				return render(request, "users/register_login.html", context={"error": "this email is already taken"})

			if User.objects.filter(username=username).exists():
				return render(request, "users/register_login.html", context={"error": "this username is already taken"})

			if password != password2:
				return render(request, "users/register_login.html", context={"error": "passwords don't match"})

			user = User(email=email, username=username, first_name=firstname, last_name=lastname)
			user.set_password(password)
			user.save()

			auth_login(request, user)
			profile = Profile(user=user)
			profile.save()

			wishlist = WishList(profile=profile)
			wishlist.save()

			return redirect("home")

	return render(request, "users/register_login.html")

@login_required(login_url="RegisterLogin")
def logoutView(request):
	logout(request)
	return redirect("home")