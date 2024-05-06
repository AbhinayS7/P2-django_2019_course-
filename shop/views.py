from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact ,Orders, OrderUpdate
from math import ceil
import json
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
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

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
    if request.method == 'POST':
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request,'shop/checkout.html')