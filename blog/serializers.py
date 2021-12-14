from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from blog.models import Post, Tag


class PostSerializer(serializers.ModelSerializer):
    tags = SlugRelatedField(queryset=Tag.objects, many=True, slug_field='name')

    class Meta:
        model = Post
        fields = '__all__'
