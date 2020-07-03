from django.shortcuts import render
from .models import bankDetails
from .serializer import bankSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response


class SnippetList(generics.ListAPIView):
    serializer_class = bankSerializer
    
    def get_queryset(self):       
        
        bank_name = self.request.query_params.get('bank_name')
        city = self.request.query_params.get('city')
        ifsc = self.request.query_params.get('ifsc')

        if ifsc != None:
            queryset = bankDetails.objects.all().filter(ifsc=ifsc)
        elif city != None and bank_name != None:
            queryset = bankDetails.objects.all().filter(city=city,bank_name=bank_name)
        elif city != None:
            queryset = bankDetails.objects.all().filter(city=city)
        elif bank_name != None:
            queryset = bankDetails.objects.all().filter(bank_name=bank_name)
        else:
            queryset = bankDetails.objects.all()
        
        if len(queryset) == 0:
            raise Http404
        return queryset

