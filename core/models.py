from django.db import models
from users.models import Profile

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	old_price = models.FloatField(null=True, blank=True)
	price = models.FloatField()
	quantity = models.IntegerField()

	def __str__(self):
		return self.title

class WishList(models.Model):
	products = models.ManyToManyField(Product, null=True, blank=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.profile.user.username}'s wishlist"

class Order(models.Model):
	products = models.ManyToManyField(Product)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.profile.user.username}'s order"