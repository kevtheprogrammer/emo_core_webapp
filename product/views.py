from django.shortcuts import render,get_object_or_404,redirect

from django.contrib import messages
import json

from django.views.generic import ListView , DetailView ,View,TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *

from stock.models import StockModel
from .models import *



class HomeListView(ListView):
    model = Product
    template_name = "index.html"
    form_class = ProductSearchForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class() 
        context["category"] = Category.objects.all() 
        context["object_list_3"] = Product.objects.all()[:3] 
        context["tags"] = Tag.objects.all() 
        return context 

class ShopListView(ListView):
    model = Product
    paginate_by = 9
    query_set = 'object_list'
    template_name = "product/listing.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro =  []
        for p in Product.objects.all():
            if p.discount > 0:
                pro.append(p)
        context["category"] = Category.objects.all() 
        context["object_list_5"] = Product.objects.all()[:5] 
        context["tags"] = Tag.objects.all() 
        context["product_discount"] = pro
        return context 

class ProductDetailView(DetailView):
    model = Product
    template_name = "product/detail.html"
    form_class = ProductForm #was cartform

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stocks = ([x.quantity for x in StockModel.objects.filter(prod=self.get_object()) ])
        prod = get_object_or_404(Product,pk=self.get_object().pk)
        is_favourite = False
        if prod.favourite.filter(id=self.request.user.id).exists():
            is_favourite = True
        context["is_favourite"] =  is_favourite
        context["category"] = Category.objects.all() 
        context["object_stock"] =  sum(stocks)
        context["object_list_3"] = Product.objects.all()[:3] 
        context["form"] = self.form_class() 
        context["tags"] = Tag.objects.all() 
        context["object_tags"] = Product.objects.filter(tags__in=self.get_object().tags.all()).distinct()  
        return context 
    
    def post(self, *args, **kwargs ):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            instance = form.save(False)
            instance.buyer = self.request.user 
            instance.item = self.get_object()
            instance.save()
        return redirect('product:cart')
        
class AboutUsView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all() 
        context["object_list_3"] = Product.objects.all()[:3] 
        context["tags"] = Tag.objects.all() 
        return context 

class FavouriteView(TemplateView):
    template_name = "product/favourite.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_prod = Product.objects.filter(favourite=self.request.user)
        context["favourite"] = my_prod
        context["category"] = Category.objects.all() 
        context["tags"] = Tag.objects.all() 
        return context 

class FavouriteToggleView(CreateView):
    model = Product
  
    def get( self, request,pk, *args, **kwargs ):
        prod = get_object_or_404(Product, pk=pk)
        if prod.favourite.filter(id=self.request.user.id).exists():
            prod.favourite.remove(request.user)
        else:
            prod.favourite.add(request.user)
        return redirect('product:favourite')            
    
class SearchProduct(ListView):
    model = Product
    template_name = 'product/results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro =  []
        for p in Product.objects.all():
            if p.discount > 0:
                pro.append(p)
        
        my_prod = Product.objects.filter(favourite=self.request.user)
        context["is_favourite"] = my_prod
        context["category"] = Category.objects.all() 
        context["object_list_5"] = Product.objects.all()[:5] 
        context["tags"] = Tag.objects.all() 
        context["product_discount"] = pro
        return context   

def product_search(request):
    form = ProductSearchForm(request.GET)
    if form.is_valid():
        products = form.filter_products(Product.objects.all())
    else:
        products = Product.objects.all()

    # Filter products with discount
    pro = [p for p in Product.objects.all() if p.discount > 0]

    context = {
        'form': form,
        'object_list': products,
        'category': Category.objects.all(),
        'object_list_5': Product.objects.all()[:5],
        'tags': Tag.objects.all(),
        'product_discount': pro,
    }

    return render(request, 'product/advance_search.html', context)
   
def whyMontenegro(request):
    template_name = 'why.html'
    context = {
        "category" : Category.objects.all(), 
    }
    return render(request, template_name, context)

def buyingProcess(request):
    template_name = 'buying_process.html'
    context = {
        "category" : Category.objects.all(), 
    }
    return render(request, template_name, context)

def Entrustment(request):
    template_name = 'entrustment.html'
    context = {
        "category" : Category.objects.all(), 
        'form': ProductForm,
    }
    return render(request, template_name, context)
 

def PropertyRequest(request):
    template_name = 'property_request.html'
    context = {
        "category" : Category.objects.all(), 
        'form': ProductRequestForm,
    }
    return render(request, template_name, context)
  