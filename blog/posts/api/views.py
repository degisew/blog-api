from rest_framework.views import APIView

from blog.posts.models import Post


class PostList(APIView):
    pass


class PostDetail(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        serilaizer = PostSerializer(posts)

        return serilaizer.data