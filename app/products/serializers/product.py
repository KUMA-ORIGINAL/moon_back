from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from ..models import Product, ProductPhoto, ProductColorPhoto
from .category import CategoryProductSerializer
from .tag import TagSerializer
from .color import ColorSerializer


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('id', 'photo', 'alt', 'order')


class ProductColorPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductColorPhoto
        fields = ('id', 'photo', 'alt', 'order')


class ColorPhotoGroupSerializer(serializers.Serializer):
    color = ColorSerializer()
    photos = ProductColorPhotoSerializer(many=True)


class ProductBaseSerializer(serializers.ModelSerializer):
    categories = CategoryProductSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    photos = ProductPhotoSerializer(many=True, read_only=True)
    banner_photo = serializers.ImageField(read_only=True)
    color_photos = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'banner_photo',
            'categories', 'tags', 'photos', 'color_photos',
        )

    @extend_schema_field(ColorPhotoGroupSerializer(many=True))
    def get_color_photos(self, obj):
        data = {}
        for photo in obj.color_photos.select_related('color').all():
            color_id = photo.color.id
            if color_id not in data:
                data[color_id] = {
                    'color': ColorSerializer(photo.color).data,
                    'photos': []
                }
            data[color_id]['photos'].append(ProductColorPhotoSerializer(photo, context=self.context).data)
        return list(data.values())


class ProductSerializer(ProductBaseSerializer):
    pass


class ProductListSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = (
            'id', 'name', 'description', 'price', 'banner_photo',
        )
