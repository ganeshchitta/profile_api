from django.shortcuts import render
import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ test api view"""
    
    def get(self, request, format=None):
        """ returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


# Create your views here.
