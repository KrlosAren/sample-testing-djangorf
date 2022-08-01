
# django rest framework
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

## models and serializers
from .models import Product
from .serializers import ProductModelSerializer


class ProductViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin):

    def get_queryset(self):

        if self.action == 'list':
            return Product.objects.all()

        return Product.objects.all()

    def get_serializer_class(self):

        if self.action in ['create', 'update', 'partial_update', 'destroy', 'retrieve']:
            return ProductModelSerializer

        return ProductModelSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            product = self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductModelSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            product = self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductModelSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):
        try:
            product = self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
