from rest_framework import serializers
from inventory.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'description',
            'image'
        )

        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {'required': True},
            'price': {'required': True},
            'image': {'required': False},
            'description': {'required': False},
            'cant': {'required': False},
        }
