from django.shortcuts import render,redirect
from .models import Product,Bill,BillItem
from .forms import ProductForm



def index(request):

    return render(request,'shop/index.html')


def add_product(request):

    form = ProductForm()

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('product_list')

    return render(request,'shop/add_product.html',{'form':form})


def product_list(request):

    products = Product.objects.all()

    return render(request,'shop/product_list.html',{'products':products})


def create_bill(request):

    products = Product.objects.all()

    if request.method == "POST":

        name = request.POST['customer']

        bill = Bill.objects.create(
            customer_name=name,
            total_amount=0
        )

        total = 0

        for product in products:

            qty = request.POST.get(str(product.id))

            if qty and int(qty) > 0:

                subtotal = product.price * int(qty)

                BillItem.objects.create(
                    bill=bill,
                    product=product,
                    quantity=qty,
                    subtotal=subtotal
                )

                total += subtotal

        bill.total_amount = total
        bill.save()

        return redirect('bill_list')

    return render(request,'shop/create_bill.html',{'products':products})


def bill_list(request):

    bills = Bill.objects.all().order_by('-date')

    return render(request,'shop/bill_list.html',{'bills':bills})

def invoice(request, id):

    bill = Bill.objects.get(id=id)

    items = BillItem.objects.filter(bill=bill)

    return render(request, 'shop/invoice.html', {
        'bill': bill,
        'items': items
    })

# Create your views here.
