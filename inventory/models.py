from django.db import models
from accounts.models import Branch
from django.utils import timezone
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    min_stock_level = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'branch')

    def __str__(self):
        return f"{self.product.name} - {self.branch.name}"

    @property
    def is_low_stock(self):
        return self.quantity <= self.product.min_stock_level

    @property
    def stock_percentage(self):
        max_stock = self.product.min_stock_level * 3
        percentage = (self.quantity / max_stock) * 100
        return min(percentage, 100)