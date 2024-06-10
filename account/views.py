from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AuthTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, SignupSerializer


class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer
    permission_classes = (AllowAny, )

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

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
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        users = self.model.objects.all()
        serializer = self.serializer(users, many=True)
        return Response(serializer.data)
    
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

