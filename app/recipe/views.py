from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from core.models import Tag

from recipe import serializers


class TagViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
        """Manage tags in the database"""
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)
        queryset = Tag.objects.all()
        serializer_class = serializers.TagSerializer


        def perform_create(self, serializer):
            """Create a new ingredient"""
            serializer.save(user=self.request.user)
    # Create your views here.