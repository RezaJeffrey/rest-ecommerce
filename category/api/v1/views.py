from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
from category.models import Category
from rest_framework import status
from .serializers import CategorySerializer, CategoryCreateSerializer
from rest_framework.permissions import IsAdminUser


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing categories.
    """
    queryset = Category.objects.all()

    def get_permissions(self):
        if not self.action == 'list':
            permission_class = [IsAdminUser]
        else:
            permission_class = []
        return [permission() for permission in permission_class]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            serializer_class = CategoryCreateSerializer
        else:
            serializer_class = CategorySerializer
        return serializer_class

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(parent=None)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def search(self, request, *args, **kwargs):
        params = self.request.query_params.get('search')
        queryset = Category.objects.filter(name__icontains=params)
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
