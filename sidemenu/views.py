# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Products

class ProductIndexView(ListView):
    model = Products
    template_name = "productindex.html"


class ProductDetailView(DetailView):
    model = Products
    template_name = "productdetail.html"
# Create your views here.
# def main_view(request):
#     return render("product.html")
