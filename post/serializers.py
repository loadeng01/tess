from rest_framework import serializers as ser
from .models import Category, Post


class PostSerializer(ser.Serializer):
    category = ser.PrimaryKeyRelatedField(queryset=Category.objects.all())
    title = ser.CharField(max_length=200)
    body = ser.CharField(allow_blank=True, allow_null=True)
    created_at = ser.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance