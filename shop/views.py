from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    n = len(products)
    no_of_slides = n//4 + ceil(n/4-(n//4))
    # params = {'products':products,'no_of_slides':no_of_slides,'range':range(1,no_of_slides)}
    # return render(request,'shop/index_shop.html',params)
    allProds=[[products, range(1, no_of_slides), no_of_slides],[products, range(1, no_of_slides), no_of_slides]]

    allProds = []
    product_categories = Product.objects.values('category')
    categories = { item['category'] for item in product_categories }
    for category in categories:
        prod=Product.objects.filter(category=category)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index_shop.html", params)

def about(request):
    return render(request,'shop/about.html')

def product_page(request, myid):
    product=Product.objects.filter(product_id=myid)
    return render(request,'shop/product_view.html', {'product':product[0]})

def tracker(request):
    return render(request,'shop/tracker.html')

def contact_us(request):
    if request.method == 'POST':
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        print(name,email,phone, desc )
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'shop/contact_us.html')

def search(request):
    return render(request,'shop/search.html')

def checkout(request):
    return render(request,'shop/checkout.html')