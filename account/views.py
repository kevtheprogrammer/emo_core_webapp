from django.shortcuts import redirect, render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserListSerializer
from .forms import CustomSignupForm
from allauth.account.views import SignupView
from .forms import SignUpForm

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserListSerializer
    # permission_classes = [permissions.IsAuthenticated]

class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserListSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



