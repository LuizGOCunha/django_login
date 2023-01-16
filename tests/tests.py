
import pytest

from django.test import TestCase

# Create your tests here.

# Scopes available for fixture:
# "function" - Run once per function
# "class" - Run once per class of tests
# "module" - Run once per module of tests
# "session" - Runs once in the whole session



def test_example(fixture_ex):
    var = fixture_ex
    assert var==1

def test_example2(fixture_ex):
    var = fixture_ex
    assert var==1

def test_example3(fixture_ex):
    var = fixture_ex
    assert var==1