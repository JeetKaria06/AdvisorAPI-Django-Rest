from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Advisor, User_new, Booking
from .serializers import AdvisorSerializer, UserSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from django.http.request import HttpRequest
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authentication import get_authorization_header
from datetime import datetime
import jwt

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def add_advisor(request):
    # print(request.data)
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):
    if request.data['password']:
        request.data._mutable = True
        hashed_password = make_password(request.data['password'])
        request.data['password'] = hashed_password
        request.data._mutable = False

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        u = User_new(email=request.data['email'], password=hashed_password)
        payload = jwt_payload_handler(u)
        token = jwt_encode_handler(payload)
        serializer.save()
        return Response(data={"id":serializer.data['id'], "token":token}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def login_user(request):
#     try:
        if User.objects.filter(email=request.data['email']).exists():
            u = User.objects.get(email=request.data['email'])
            if check_password(request.data['password'], u.password):
                payload = jwt_payload_handler(u)
                token = jwt_encode_handler(payload)
                return Response(data={"id":u.id, "token":token}, status=status.HTTP_200_OK)
            return Response(data={"Error":"Email and Password Combination doesn't exist."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(data={"Error":"Email and Password Combination doesn't exist."}, status=status.HTTP_401_UNAUTHORIZED)
#     except:
#         return Response(data={"Error":"Enter email and password both"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getlist_advisor(request, id):
    token = get_authorization_header(request).decode('utf-8').split(' ')[1]
    decoded = jwt.decode(token, settings.SECRET_KEY)
    print(decoded['user_id'])
    if str(decoded['user_id'])==id:
        queryset = Advisor.objects.all()
        serializer = AdvisorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(data={'Error':'Token used is not yours.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_advisor(request, user_id, advisor_id):
    if request.data['booking_time']:
        token = get_authorization_header(request).decode('utf-8').split(' ')[1]
        decoded = jwt.decode(token, settings.SECRET_KEY)
        print(decoded['user_id'])
        if str(decoded['user_id'])==user_id:
            u = User_new.objects.get(id=user_id)
            a = Advisor.objects.get(id=advisor_id)
            b = Booking(booking_time=datetime.strptime(request.data['booking_time'], '%Y-%m-%d %H:%M:%S'), user=u, advisor=a)
            b.save()
            return Response(data={"message":"Done"}, status=status.HTTP_200_OK) 
        
        return Response(data={'Error':'Token used is not yours.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={'Error':'Enter booking time'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_calls(request, user_id):
    token = get_authorization_header(request).decode('utf-8').split(' ')[1]
    decoded = jwt.decode(token, settings.SECRET_KEY)
    print(decoded['user_id'])
    if str(decoded['user_id'])==user_id:
        u = User_new.objects.get(id=decoded['user_id'])
        queryset = Booking.objects.filter(user=u)
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(data={'Error':'Token used is not yours.'}, status=status.HTTP_400_BAD_REQUEST)
