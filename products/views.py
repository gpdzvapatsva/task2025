from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import products
from .forms import products
from .forms import ProductForm


# Create your views here.
def index(request):
    myprod = products.objects.all().order_by('name')
    context = {'myprod': myprod}
    return render(request, 'index.html', context)


# Adding a new product from the controls
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # you can add a record added successfully
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


# Delete products
def delete(request, pk):
    product = get_object_or_404(products, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')  # we can use httpresponse to display message
    return render(request, 'delete.html', {'product': product})

def metrics(request):
    return HttpResponse("Metrics data or dashboard goes here.")