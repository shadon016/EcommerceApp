from django.shortcuts import render
from .models import Products

def home(request):
    product=Products.objects.all()
    context={
        "product":product,
    }
    return render(request, 'home/index.html',context)
