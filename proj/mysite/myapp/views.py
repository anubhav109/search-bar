from django.shortcuts import render

# Create your views here.
from .models import Product

def search(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        results = Product.objects.filter(name__icontains=query)
    
    return render(request, 'search.html', {'results': results})
