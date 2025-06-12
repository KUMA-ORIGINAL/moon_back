from rest_framework import serializers
from ..models import Product, ProductPhoto
from .category import CategoryProductSerializer
from .tag import TagSerializer
from .color import ColorSerializer


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('id', 'photo', 'alt', 'order')


class ProductBaseSerializer(serializers.ModelSerializer):
    categories = CategoryProductSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    color = ColorSerializer(read_only=True)
    photos = ProductPhotoSerializer(many=True, read_only=True)
    banner_photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'banner_photo',
            'color', 'categories', 'tags', 'photos',
        )


class ProductSerializer(ProductBaseSerializer):
    pass


class ProductListSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = (
            'id', 'name', 'description', 'price', 'banner_photo',
        )
