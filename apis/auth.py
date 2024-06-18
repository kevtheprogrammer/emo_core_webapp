from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from account.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomLoginView(TokenObtainPairView):
    
    def post(self, request):
        email = request.data.get('email')
        # phone = request.data.get('phone')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user:
            # Token payload
            payload = {
                'id': user.id,
                'email': user.email,
                'phone': user.phone,
                'first_name': user.first_name,
                'last_name': user.last_name,
                # Assuming avatar is an ImageField
                # 'avatar': user.avatar.url if user.avatar else None,
                'dob': user.dob.isoformat() if user.dob else None,
            }

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            access_token = RefreshToken.for_user(user)
            access_token['payload'] = payload
            access_token = str(access_token.access_token)
            refresh_token = str(refresh)

            return Response(
                {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                },
                status=status.HTTP_200_OK
            )
        
        return Response({'error': 'Invalid credentials'}, status=401)
    
    
class CustomTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        # Extract the refresh token from the request data
        refresh_token = request.data.get('refresh_token')

        # Check if the refresh token is missing
        if not refresh_token:
            return Response({'error': 'Refresh token is missing'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Validate the refresh token
            token = RefreshToken(refresh_token)
            token.verify()
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        user = token.payload.get('user_id')  # Get user from token payload

        if user is not None:
            user = User.objects.get(pk=user)  # Retrieve user object
            payload = {
                'email': user.email,
                'phone_number': user.phone_number,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'dob': user.dob.isoformat() if user.dob else None,
            }
            # Generate JWT tokens with custom payload
            new_access_token = RefreshToken.for_user(user)
            new_access_token.payload.update(payload=payload)  # Update token payload

            new_refresh_token = RefreshToken.for_user(user)

            return Response(
                {
                    'access_token': str(new_access_token),
                    'refresh_token': str(new_refresh_token)
                },
                status=status.HTTP_200_OK
            )
        
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    