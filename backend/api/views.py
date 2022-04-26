from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
@ api_view(["POST"])
def api_home(request,*args,**kwags):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance=serializer.save()
        print(serializer.data)
        return Response(serializer.data)