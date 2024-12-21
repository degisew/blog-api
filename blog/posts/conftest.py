from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
import pytest
from model_bakery import baker

User = get_user_model()

@pytest.fixture
def user() -> AbstractUser:
    return baker.make(User)
