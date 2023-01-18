
import pytest

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


def test_if_we_can_create_a_user(return_test_user):
    user = return_test_user
    count = User.objects.count()
    assert count == 1

def test_if_created_user_has_correct_fields(return_test_user):
    user = return_test_user
    assert user.username == "usernametest"
    assert user.email == "test@test.com"
    assert user.check_password('passwordtest') is True

@pytest.mark.django_db
# The above decorator can be used to create a db inside a test
def test_if_we_can_access_other_tests_db():
    count = User.objects.count()
    assert count != 1


