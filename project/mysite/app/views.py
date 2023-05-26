
from django.shortcuts import render
from django.http import JsonResponse
from .models import Names

def index(request):
    return render(request, 'index.html')

def get_names(request):
    search = request.GET.get('search')
    payload = []

    if search:
        objs = Names.objects.filter(name__startswith=search)
        payload = [{'name': obj.name} for obj in objs]

    return JsonResponse({'data': payload})
