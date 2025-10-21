from django.shortcuts import render, redirect, get_object_or_404
from .models import products
from .forms import products
from .forms import ProductForm

"""
products.views
--------------
HTTP view handlers for the products app.

Provides:
- index: list products on the storefront.
- add_product: show and process the product creation form.
- (delete view expected below)
"""

def index(request):
    """Render the storefront homepage.

    Queries all products ordered by name and renders 'index.html'
    with context {'myprod': queryset}.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: Rendered homepage.
    """
    myprod = products.objects.all().order_by('name')
    context = {'myprod': myprod}
    return render(request, 'index.html', context)


def add_product(request):
    """Handle the add-product form.

    - GET: render an empty ProductForm.
    - POST: validate form (including request.FILES) and save the product,
      then redirect to the index page.

    Notes:
    - The form should include file inputs if your Product model has image fields.
    - After saving, the redirect prevents duplicate submissions on refresh.

    Args:
        request (HttpRequest)

    Returns:
        HttpResponse or HttpResponseRedirect
    """
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
