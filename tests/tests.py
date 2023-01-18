
import pytest

from django.contrib.auth.models import User


def test_if_we_can_create_a_user(return_test_user):
    user = return_test_user
    count = User.objects.count()
    assert count == 1

@pytest.mark.django_db
# The above decorator can be used to create a db inside a test
# however, i already created a fixture that creates a db for me,
# so we are using that instead
def test_if_we_can_access_other_tests_db():
    count = User.objects.count()
    assert count != 1

def test_if_we_can_check_users_password(return_test_user):
    user = return_test_user
    assert user.check_password('passwordtest') is True