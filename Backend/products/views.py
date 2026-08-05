from rest_framework import viewsets, status
from rest_framework.response import Response 
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Category, product
from .serializer import (
    LoginSerializer,
    CategorySerializer,
    ProductSerializer,
)


# Create your views here.
####========LoginView======####
class LoginView(viewsets.ViewSet):
    
    
    """ Handle User authentication with JWT Tokens
        POST /api/login/ """
    
    def create(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {
                    "detail": "Invalid username or password."
                },status=status.HTTP_401_UNAUTHORIZED
            )    
        
        if not user.check_password(password):
            return Response(
                {
                    "detail": "Password is wrong."
                },status=status.HTTP_401_UNAUTHORIZED
            )
        
        
        # Generate JWT Tokens
        # Create a Refresh Token for the logged-in user
        refresh = RefreshToken.for_user(user)

         # Get the Access Token from the Refresh Token
        access = refresh.access_token

        # Send both tokens to the client
        return Response(
        {
        "access": str(access),
        "refresh": str(refresh),
        },status=status.HTTP_200_OK)    
        
        
####=======Categories(Readonly Viewset)==========#
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]        
    
####=====Products (Full CRUD ViewSet)======####
class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
                   