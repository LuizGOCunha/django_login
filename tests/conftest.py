# This test is used to configure some options for our tests
# Mainly i can use it to share our fixtures with pytest
# Here are some details taken from chatCPT:

"""
what are conftest configuration options ?
pytest uses several configuration options that can be specified in a 
conftest.py file to configure the behavior of the test runner. Some 
of the most common options include:

- pytest.mark: This allows you to mark test functions with custom tags,
which can be used to selectively run tests based on their marks.
- pytest.fixture: This can be used to define fixtures that can be used
to provide test functions with resources or data.
- pytest.usefixtures: This can be used to specify that a test function
should use one or more fixtures.
- pytest.raises: This can be used to assert that a specific exception 
is raised during the execution of a test function.
- pytest.parametrize: This can be used to run a single test function 
multiple times with different input data.
- pytest.skip and pytest.xfail: These can be used to skip or mark a 
test function as expected to fail.
- pytest.approx: This can be used to compare two float numbers with a
specific tolerance .
- pytest.hookimpl: This can be used to define custom hooks that can be
executed at specific points during the test run.

These are some of the most common options, but there are many more 
that can be used to customize the behavior of the test runner.
"""
import pytest
from django.contrib.auth.models import User

# Scopes available for fixture:
# "function" - Run once per function
# "class" - Run once per class of tests
# "module" - Run once per module of tests
# "session" - Runs once in the whole session

@pytest.fixture(scope="session")
def fixture_ex():
    """
    A fixture is a function that runs before a python test if its name is given
    as an argument. It is useful for setting up an environment for the testing.
    """
    print("*******************")
    var = 1
    yield var

@pytest.fixture(scope='function')
# the 'db' fixture can be passed when creating a fixture, so we can create a database with it
def return_test_user(db):
    user = User.objects.create_user('usernametest','test@test.com', 'passwordtest')
    return user