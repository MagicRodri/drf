from django.shortcuts import render
from rest_framework import generics, serializers

from app.models import Entity
from app.serializers import EntitySerializer

# Create your views here.


class EntityList(generics.ListCreateAPIView):
    """
        List all entities or create a new one
    """
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def perform_create(self, serializer):
        """ 
            Set 'modified_by' field to current user
        """
        user = self.request.user
        if not user.is_authenticated:
            raise serializers.ValidationError('User not authenticated')

        serializer.save(modified_by=user)