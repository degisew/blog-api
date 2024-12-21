import pytest
from model_bakery import baker
from django.core.exceptions import ValidationError
from blog.posts.models import Post


@pytest.mark.django_db
def test_expected_to_create_post_objects_successfully() -> None:
    post = baker.make(Post, title="Django for APIs")

    assert post.id is not None
    assert post.title == "Django for APIs"
    assert str(post) == post.title


@pytest.mark.django_db
def test_expected_to_fail_on_invalid_data(user) -> None:
    post = Post.objects.create(title='', author=user, body='')

    with pytest.raises(ValidationError) as execinfo:
        post.full_clean()
