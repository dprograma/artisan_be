import json
import bcrypt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

# local modules
from .serializers import UserSerializer
from .models import User

# Create your views here.


@api_view(['POST'])
def login(request): 
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return Response({"errCode": 0, "errMsg": "User Successfully Logged in."})
            else:
                return Response({"errCode": 1, "errMsg": "Invalid username or password."})
        except User.DoesNotExist:
            return Response({"errCode": 1, "errMsg": "User does not exist."})


@api_view(['POST'])
def register(request):
    try:
        if request.method == 'POST':
            query = {}
            username = request.data.get('username').lower()
            email = request.data.get('email').lower()
            password = request.data.get('password')
            query['username'] = username
            query['password'] = make_password(password)
            query['email'] = email
            user = User.objects.create(**query)
            getuser = User.objects.filter(email=email)
            serialized = UserSerializer(getuser, many=True)
            return Response({"errCode": 1, "errMsg": "User Successfully Created.", "result": serialized.data})
    except Exception as e:
        return Response({"errCode": 1, "errMsg": "Something went wrong. Please try again later. "})
