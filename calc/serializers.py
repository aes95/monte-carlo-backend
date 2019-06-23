from .models import Index
from rest_framework import serializers

class IndexSerializer(serializers.HyperlinkedModelSerializer):
        
    class Meta:
        model = Index
        fields = ('id', 'url', 'mo_return', 'adj_close', 'high', 'low', 'date', 'index_name')