from django.shortcuts import render
from django.http import HttpResponse
from .models import Index
from rest_framework import viewsets
from .serializers import IndexSerializer
from url_filter.integrations.drf import DjangoFilterBackend

class IndexViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows returns to be viewed'''
    queryset = Index.objects.all()
    serializer_class = IndexSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'date', 'index_name']
    #lookup_field = 'index_name'