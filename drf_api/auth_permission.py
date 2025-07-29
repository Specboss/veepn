from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

from app.posts.models import Post
from drf_api.posts.post_service import AuthorPosts, UserPosts


class RolePermission(BasePermission):
    """
    Базовый клас
    """
    required_roles = []

    def has_permission(self, request, view):
        user = request.user
        return (
                user and user.is_authenticated and
                hasattr(user, 'role') and
                user.role in self.required_roles
        )


class Author(RolePermission):
    required_roles = ['author']


class User(RolePermission):
    required_roles = ['user']


class CanAccessPost(BasePermission):
    def has_permission(self, request, view):
        method = request.method
        if method == "GET":
            post_id = request.query_params.get("post")
        elif method in ["POST", "DELETE"]:
            post_id = request.data.get("post")
        else:
            return True
        if not post_id or not request.user.is_authenticated:
            raise PermissionDenied("Post not found.")
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise PermissionDenied("Post not found.")
        user = request.user
        allowed_posts = Post.objects.none()

        if user.role == 'author':
            allowed_posts |= AuthorPosts(user=user).get_queryset()

        # Даже если автор — он может быть подписчиком
        allowed_posts |= UserPosts(user=user).get_queryset()
        if not allowed_posts.filter(id=post.id).exists():
            raise PermissionDenied("Can't access this post.")
        return True
