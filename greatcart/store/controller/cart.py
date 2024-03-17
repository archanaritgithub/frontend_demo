from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django import views
from store.models import Product, Cart

def addtocart(requset):
    if requset.method == 'POST':
        if requset.user.is_authenticated:
            prod_id = int(requset.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=requset.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in Cart"})
                else:
                    prod_qty  = int(requset.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty :
                        Cart.objects.create(user=requset.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': " Product Added Successfully "})
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.quantity) +"quantity available"})
            else:
                return JsonResponse({'status':"No Such Product found"})
        else:
            return ({'status':"Login to Continue"})        
    return redirect('homee')

def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request,'apps/products/cart.html',context)