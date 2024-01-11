from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q


from .models import *
from stock.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'thumb','is_sold','name','description','price','discount','category','slug'
        ]
  
class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = PropertyRequst
        fields = [
            'price','reason','description','square_meter','property_type','bedrooms','bathrooms','total_rooms','area'
        ]
  
 
class StockForm(forms.ModelForm):
    class Meta:
        model = StockModel
        fields = [
            'prod','quantity','slug'
            ]


class StockEditForm(forms.ModelForm):
    class Meta:
        model = StockModel
        fields = [
            'quantity',
        ]

 

class ProductSearchForm(forms.Form):
    # name = forms.CharField(required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)
    min_square_meter = forms.IntegerField(required=False, min_value=0)
    max_square_meter = forms.IntegerField(required=False, min_value=0)
    property_type = forms.ChoiceField(choices=Product.TYPES, required=False)
    total_rooms = forms.IntegerField(required=False, min_value=0)
    reason = forms.ChoiceField(choices=Product.TYPE_CHOICES, required=False)

    def filter_products(self, queryset):
        # Initial queryset
        products = Product.objects.all()

        # Apply filters based on form inputs
        # name = self.cleaned_data.get('name')
        # if name:
        #     products = products.filter(name__icontains=name)

        min_price = self.cleaned_data.get('min_price')
        max_price = self.cleaned_data.get('max_price')
        if min_price is not None and max_price is not None:
            products = products.filter(price__range=(min_price, max_price))

        min_square_meter = self.cleaned_data.get('min_square_meter')
        max_square_meter = self.cleaned_data.get('max_square_meter')
        if min_square_meter is not None and max_square_meter is not None:
            products = products.filter(square_meter__range=(min_square_meter, max_square_meter))

        property_type = self.cleaned_data.get('property_type')
        if property_type:
            products = products.filter(property_type=property_type)

        total_rooms = self.cleaned_data.get('total_rooms')
        if total_rooms is not None:
            products = products.filter(total_rooms=total_rooms)

        region = self.cleaned_data.get('region')
        if region:
            products = products.filter(region=region)

        reason = self.cleaned_data.get('reason')
        if reason:
            products = products.filter(reason=reason)

        return products
