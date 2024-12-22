from django.urls import path
from blog.posts.api.views import PostList, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
]
