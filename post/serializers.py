from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from .models import Post

class PostListSerializer(ModelSerializer):
    url =HyperlinkedIdentityField(view_name='posts-api:detail')
    class Meta:
        model=Post
        fields=[
            'name',
            'email',
            'content',
            'url',
            'date',
          
        ]

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=[
            'name',
            'email',
            'content',
            'date',
        ]