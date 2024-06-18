from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.models import User
from django.http import Http404, HttpResponse, request
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from product.models import Product  
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# class UserListView(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('date_joined')
#     serializer_class = UserListSerializer
#     # permission_classes = [permissions.IsAuthenticated]

# class UserDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = UserListSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ViewSet):

    model = User
    serializer = UserSerializer

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Http404


    def list(self, request):
        users = self.model.objects.all()
        serializer = self.serializer(users, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        user = self.model.objects.get(pk=pk)
        serializer = self.serializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        try:
            user =self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "User Updated Successfully",
                "data" : serializer.data})
        
        error_messages = {field: error[0] for field, error in serializer.errors.items()}
        return Response({"error": error_messages}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            user = self.get_object(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        user = self.model.objects.all()
        serializer = self.serializer(user, many=True)
        return Response({
            "message" : "delete user with sucess",
            "data" : serializer.data}, status=status.HTTP_204_NO_CONTENT)
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list','create', 'retrieve', 'update']:
            permission_classes = [IsAuthenticated]
        elif self.action in 'destroy':
            permission_classes = [IsAuthenticated]   
        else:
            permission_classes = [AllowAny] # [IsAdminUser]
        return [permission() for permission in permission_classes]

# product api viewsets


class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductCreationSerializer
    serializer = ProductSerializer
    model = Product
	
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def list(self, request):
        product = self.model.objects.all()
        serializer = self.serializer(product, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        product = self.model.objects.get(pk=pk)
        serializer = self.serializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        try:
            product = self.get_object(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product = self.model.objects.get(pk=pk)
        serializer = self.serializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            product = self.get_object(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        products = self.model.objects.all()
        serializer = self.serializer(products, many=True)
        return Response({
            "message": "Deleted product successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list','create', 'retrieve', 'update']:
            permission_classes = [IsAuthenticated]
        elif self.action in 'destroy':
            permission_classes = [IsAuthenticated]   
        else:
            permission_classes = [AllowAny] # [IsAdminUser]
        return [permission() for permission in permission_classes]
    

# class InvoiceViewSet(viewsets.ViewSet):
    
#     serializer = InvoiceSerializer
#     model = Invoice
#     def get_object(self ,pk):
#         try:
#             return self.model.objects.get(pk=pk)
#         except self.model.DoesNotExist:
#             return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        
         
#     def list(self, request):
#         invoice = Invoice.objects.all()
#         serializer = self.serializer(invoice, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = self.serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, stutus=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         invoice = Invoice.objects.get(pk=pk)
#         serializer = self.serializer(invoice)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         try:
#             invoice = self.get_object(pk=pk)
#         except self.model.DoesNotExist:
#             return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         invoice = self.model.objects.get(pk=pk)
#         serializer = self.serializer(invoice, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk=None):
#         try:
#             invoice = self.get_object(pk=pk)
#         except self.model.DoesNotExist:
#             return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         invoice.delete()
#         invoice = self.model.objects.all()
#         serializer = self.serializer(invoice, many=True)
#         return Response({
#             "message": "Deleted User object with success",
#             "data": serializer.data,
#         }, status=status.HTTP_200_OK)
    
#     def get_permissions(self):

#         if self.action == 'list':
#             permission_classes = [IsAuthenticated]
#         elif self.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
#             permission_classes = [IsAuthenticated]
#         else:
#             permission_classes = [AllowAny]  # [IsAdminUser]
#         return [permission() for permission in permission_classes]


# class CompanyViewSet(viewsets.ViewSet):
#     serializer = CompanySerializer
#     model = Company
    
#     def get_object(self, pk):
#         try:
#             return self.model.objects.get(pk=pk)
#         except self.model.DoesNotExist:
#             return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        
#     def list(self, request):
#         company = self.model.objects.all()
#         serializer = self.serializer(company, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = self.serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, stutus=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         company = Company.objects.get(pk=pk)
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         try:
#             company = self.get_object(pk=pk)
#         except self.model.DoesNotExist:
#             return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         company = self.model.objects.get(pk=pk)
#         serializer = self.serializer(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk=None):
#         try:
#             company = self.get_object(pk=pk)
#         except self.model.DoesNotExist:
#             return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         company.delete()
#         company = self.model.objects.all()
#         serializer = self.serializer(company, many=True)
#         return Response({
#             "message": "Deleted User object with success",
#             "data": serializer.data,
#         }, status=status.HTTP_200_OK)
    
# class CategoryViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         category = Category.objects.all()
#         serializer = CompanySerializer(category, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, stutus=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CompanySerializer(category)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CompanySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# # email viewset


# class EmailingViewSet(viewsets.ModelViewSet):
    
#     def list(self, request):
#         mail = Emailing.objects.all()
#         serializer = EmailingSerializer(mail, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmailingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         mail = Emailing.objects.get(pk=pk)
#         serializer = EmailingSerializer(mail)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         user = Emailing.objects.get(pk=pk)
#         serializer = EmailingSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk=None):
#         mail = Emailing.objects.get(pk=pk)
#         mail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# # sales and markets


# class CustomerViewSet(viewsets.ViewSet):
    
#         def list(self, request):
#             customers = Customer.objects.all()
#             serializer = CustomerSerializer(customers, many=True)
#             return Response(serializer.data)
        
#         def create(self, request):
#             serializer = CustomerSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def retrieve(self, request, pk=None):
#             customer = Customer.objects.get(pk=pk)
#             serializer = CustomerSerializer(customer)
#             return Response(serializer.data)
        
#         def update(self, request, pk=None):
#             customer = Customer.objects.get(pk=pk)
#             serializer = CustomerSerializer(customer, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def delete(self, request, pk=None):
#             customer = Customer.objects.get(pk=pk)
#             customer.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
        
# class SaleViewSet(viewsets.ViewSet):
    
#         def list(self, request):
#             sale = Sale.objects.all()
#             serializer = SaleSerializers(sale, many=True)
#             return Response(serializer.data)
        
#         def create(self, request):
#             serializer = SaleSerializers(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def retrieve(self, request, pk=None):
#             sale = Sale.objects.get(pk=pk)
#             serializer = SaleSerializers(sale)
#             return Response(serializer.data)
        
#         def update(self, request, pk=None):
#             sale = Sale.objects.get(pk=pk)
#             serializer = SaleSerializers(sale, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def delete(self, request, pk=None):
#             sale = Sale.objects.get(pk=pk)
#             sale.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

# #ticket


# class TicketViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         ticket = Ticket.objects.all()
#         serializer = TicketSerializer(ticket, many=True)
#         return Response(serializer.data)
    
    
#     def create(self, request):
#         serializer = TicketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         ticket = Ticket.objects.get(pk=pk)
#         serializer = TicketSerializer(ticket)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         ticket = Ticket.objects.get(pk=pk)
#         serializer = TicketSerializer(ticket, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk=None):
#         ticket = Ticket.objects.get(pk=pk)
#         ticket.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class CategoryViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
