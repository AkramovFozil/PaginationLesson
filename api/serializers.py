from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title", "description", "category", "created_at"]

    def to_representation(self, instance):
        """
        GET so‘rovlar uchun categoryni nested formatda qaytaradi.
        """
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation

    def to_internal_value(self, data):
        """
        POST so‘rovlar uchun categoryni ID formatida qabul qiladi.
        """
        internal_value = super().to_internal_value(data)
        if 'category' in data:
            try:
                category = Category.objects.get(id=data['category'])
                internal_value['category'] = category
            except Category.DoesNotExist:
                raise serializers.ValidationError({'category': 'Invalid author ID.'})
        return internal_value