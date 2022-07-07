from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
# def test_homepage_access():
#     url = reverse('home')
#     assert url == "/"

class Genre:
    def __init__(self, title):
        self.title = title

def test_classes_compare():
    g1 = Genre("Action")
    g2 = Genre("Action")
    assert g1.title == g2.title


def test_classes_comp():
    ge1 = Genre("Action")
    ge2 = Genre("Romance")
    assert ge1.title == ge2.title