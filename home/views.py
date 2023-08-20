from django.shortcuts import render
from .models import *
# Create your views here.
def show_product(request):
    objs = Product.objects.all()
    context = {"objs":objs}
    return render(request, "home.html", context)
