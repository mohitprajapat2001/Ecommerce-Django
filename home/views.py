from django.shortcuts import render, redirect
from .models import products,carasouelimage
from math import ceil

def home(request):
    Products = products.objects.all()
    CarasouelImage = carasouelimage.objects.all()
    n = len(Products)
    slides = n//4 + ceil((n/4 - n//4))
    zipprice = totprice(Products)
    params = {'slides':slides, "range":range(slides),"zipprice":zipprice, "Products":Products, "CarasouelImage": CarasouelImage}
    return render(request, "HTML/home.html",params)

def searchproduct(request):
    if request.method == "POST":
        search = request.POST['searchbar']
        namesearch = products.objects.filter(name = search)
        categorsearch = products.objects.filter(category = search)
        myprod = list(namesearch) + list(categorsearch)
        myprod = products.objects.filter(pk__in=[item.pk for item in myprod])
        print(myprod)
        for i in myprod:
            print(i)
        params = {"myprod":myprod}
        return render(request, "HTML/category.html", params)
    
def prodview(request, prod):
    myprod = products.objects.get(id = prod)
    temp = myprod.price
    temp = int(temp + (temp * (myprod.discount/100)))
    i = myprod.description
    description = i.split(";")
    myparam = {"myprod": myprod, "temp": temp, "description": description}
    return render(request, "HTML/ViewProduct.html", myparam)

def categoryview(request, category):
    myprod = products.objects.filter(category = category)
    zipprice =  totprice(myprod)
    my = {"myprod": myprod, "zipprice" : zipprice}
    return render(request, "HTML/category.html", my)

def totprice(myprod):
    totalprice = []
    id = [] 
    for i in myprod:
        temp = i.price
        temp = int(temp + (temp * (i.discount/100)))
        totalprice.append(temp)
        temp = int(i.id)
        id.append(temp)
    return dict(zip(id,totalprice))