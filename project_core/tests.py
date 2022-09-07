from django.test import Client
from django.urls import reverse
import pytest

client = Client()


@pytest.mark.django_db
def test_home_view():
    result = client.get(reverse('home'))
    assert result.status_code == 200
