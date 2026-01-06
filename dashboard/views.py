from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventory.models import Product, Stock
from accounts.models import Branch, Profile
from django.db.models import Sum
# Create your views here.
@login_required
def dashboard(request):
    profile = request.user.profile
    if profile.role == "admin":
        stocks = Stock.objects.all()
    else:
        stocks = Stock.objects.filter(branch=profile.branch)
    total_products = stocks.values('product').distinct().count()
    total_stock = stocks.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_branches = Branch.objects.count()
    low_stock = stocks.filter(quantity__lte=10)

# ...existing code...
    return render(request, 'dashboard.html', {
        'total_products': total_products,
        'total_branches': total_branches,
        'total_stock': total_stock,
        'stocks': stocks,
        'low_stock': low_stock,
    })
# ...existing code...