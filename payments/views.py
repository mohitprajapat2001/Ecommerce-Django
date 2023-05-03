from django.shortcuts import render, redirect,HttpResponse
from home.models import products
from .models import userpayments
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User,auth
from accounts.models import user as myuser
import json


def payments(request, id):
    if request.user.is_authenticated:
        current_user = myuser.objects.get(id = request.user.id)
        my_product = products.objects.get(id = id)
        user_cart = userpayments()
        user_cart.userid = current_user.id
        user_cart.name = current_user.name
        user_cart.username = current_user.username
        user_cart.address = current_user.address
        user_cart.cart = True
        user_cart.wishlist = False
        user_cart.phone = current_user.phone
        user_cart.product_name = my_product.name
        user_cart.product_category = my_product.category
        user_cart.price = my_product.price
        user_cart.product_id = my_product.id
        user_cart.tax = my_product.tax
        user_cart.discount = my_product.discount
        user_cart.available = my_product.available
        user_cart.save()
        return redirect("/Cart")
    else:
        messages.info(request, "Login Required")
        return redirect("/")

def wishlist(request, id):
    if request.user.is_authenticated:
        current_user = myuser.objects.get(id = request.user.id)
        my_product = products.objects.get(id = id)
        user_cart = userpayments()
        user_cart.userid = current_user.id
        user_cart.name = current_user.name
        user_cart.username = current_user.username
        user_cart.address = current_user.address
        user_cart.wishlist = True
        user_cart.phone = current_user.phone
        user_cart.product_id = my_product.id
        user_cart.product_name = my_product.name
        user_cart.product_category = my_product.category
        user_cart.price = my_product.price
        user_cart.tax = my_product.tax
        user_cart.discount = my_product.discount
        user_cart.available = my_product.available
        user_cart.save()
        return redirect("/wishlistView")
    else:
        messages.info(request, "Login Required")
        return redirect("/")


def cart(request):
    if request.user.is_authenticated:
        try:
            cart_view = userpayments.objects.filter(userid = myuser.objects.get(id = request.user.id).id)
            return render(request, "HTML/cart.html", {"cart_view" : cart_view})
        except Exception as e:
            messages.info(request, "Update Your Profile First")
            return redirect("/")
        
    else:
        messages.info(request, "Login Required")
        return redirect("/")


def wishlistView(request):
    if request.user.is_authenticated:
        try:     
            Products = products.objects.all()
            wishlist_view = userpayments.objects.filter(userid = myuser.objects.get(id = request.user.id).id)
            return render(request, "HTML/wishlist.html", {"wishlist_view" : wishlist_view, "Products" : Products})
        except Exception as e:
            messages.info(request, "Update Your Profile First")
            return redirect("/")
    else:
        messages.info(request, "Login Required")
        return redirect("/")


def deleteitem(request, id):
    usercart = userpayments.objects.get(id = id)
    usercart.cart = False
    usercart.wishlist = False
    usercart.quantity = 0
    usercart.save()
    return redirect("/Cart")

def wishlistdeleteitem(request, id):
    usercart = userpayments.objects.get(id = id)
    usercart.cart = False
    usercart.wishlist = False
    usercart.quantity = 0
    usercart.save()
    return redirect("/wishlistView")

def paymentpage(request):
    cart_view = userpayments.objects.filter(userid = request.user.id)
    if request.method == "POST":
        for i in cart_view:
            if request.POST.get(f"quantity{i.id}") is not None:
                i.quantity = request.POST.get(f"quantity{i.id}")
                i.save()
    grandtotal =  0
    for i in cart_view:
        if i.cart is True:
            grandtotal += int(i.price)*int(i.quantity)
    return render(request, "HTML/paypal.html", {"grandtotal":grandtotal})
    
def ordercomplete(request):
    body = json.loads(request.body)
    print("Order Confirm:", body)
    cart_views = userpayments.objects.filter(userid = request.user.id)
    for cart_view in cart_views:
        if cart_view.cart is True:
            cart_view.cart = False
            cart_view.paymentid = body['transaction_id']
            cart_view.paymentstatus = True
            cart_view.save()
    return JsonResponse({'message': 'Order completed'})

def myorders(request):
    cart_views = userpayments.objects.filter(userid = request.user.id)
    prices = productprice(cart_views)
    params = {"cart_views" : cart_views, "prices" : prices}
    return render(request, "HTML/myorders.html", params)

def productprice(cart_views):
    temp = 0
    orderprice = []
    priceid = []
    for i in cart_views:
        temp = int(i.quantity)*int(i.price)
        orderprice.append(temp)
        priceid.append(int(i.product_id))
    return dict(zip(priceid, orderprice))