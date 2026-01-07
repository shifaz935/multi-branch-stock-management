from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.contrib import messages
from .models import Product, Stock
from accounts.models import Profile

def get_user_profile(user):
    """Helper function to safely get user profile"""
    try:
        return user.profile
    except Profile.DoesNotExist:
        return None

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

@login_required
def stock_list(request):
    profile = Profile.objects.get(user=request.user)

    # Admin → See all stocks
    if profile.role == 'admin':
        stocks = Stock.objects.all()

    # Manager / Staff → Only their branch
    else:
        stocks = Stock.objects.filter(branch=profile.branch)

    return render(request, 'inventory/stock_list.html', {
        'stocks': stocks
    })

@login_required
@login_required
def add_stock(request):
    profile = get_user_profile(request.user)
    
    if not profile:
        messages.error(request, 'Your profile is not set up. Contact administrator.')
        return redirect('dashboard')

    if not profile.branch:
        messages.error(request, 'You must be assigned to a branch.')
        return redirect('dashboard')

    products = Product.objects.all()

    if request.method == "POST":
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')

        if not product_id or not quantity:
            messages.error(request, 'Product and quantity are required.')
            return redirect('add_stock')
        

        try:
            quantity = int(quantity)
            if quantity < 0:
                messages.error(request, 'Quantity must be positive.')
                return redirect('add_stock')
        except ValueError:
            messages.error(request, 'Invalid quantity.')
            return redirect('add_stock')

        product = get_object_or_404(Product, id=product_id)

        stock, created = Stock.objects.get_or_create(
            product=product,
            branch=profile.branch,
            defaults={'quantity': quantity}
        )

        if not created:
            stock.quantity = quantity
            stock.save()

        messages.success(request, f'Stock updated for {product.name}')
        return redirect('stock_list')

    return render(request, 'inventory/add_stock.html', {'products': products})

@login_required
def add_product(request):
    profile = get_user_profile(request.user)
    
    if not profile:
        messages.error(request, 'Your profile is not set up. Contact administrator.')
        return redirect('product_list')

    if profile.role != 'admin':
        messages.error(request, 'Only admins can add products.')
        return redirect('product_list')

    ProductForm = modelform_factory(Product, fields='__all__')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'inventory/add_product.html', {'form': form})
def price_history(request, product_id):
    product = Product.objects.get(id=product_id)
    history = product.price_history.order_by('-changed_at')

    return render(request, 'inventory/price_history.html', {
        'product': product,
        'history': history
    })
