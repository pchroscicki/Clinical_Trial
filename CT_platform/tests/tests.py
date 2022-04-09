from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

# Create your tests here.


def test_sum():
    assert 2 + 2 == 4

def test_empty():
    assert True
