from  rest_framework.generics import CreateAPIView,ListAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
from .serializers import PostListSerializer,PostDetailSerializer
from .models import Post
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination
from django.db.models import Q

# Create your views here.
class PostCreateAPIView(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializer

class PostListAPIview(ListAPIView):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostListSerializer
    permission_classes=[AllowAny]
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Post.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(name__icontains=query)|
                    Q(email__icontains=query)
                    ).distinct()
        return queryset_list
  

class PostDetailAPIView(RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializer

class PostUpdateAPIView(UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializer

class PostDeleteAPIView(DestroyAPIView):
    queryset=Post.objects.all()
    serializer_View=PostDetailSerializer

