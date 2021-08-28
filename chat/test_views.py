from django.test import TestCase
from django.urls import path
from django import urls

import pytest

@pytest.mark.parametrize(param, [
    ('chatroom'),
    ('index'),
    ('home')
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp     = client.get(temp_url)
    return resp.status_code == 200

@pytest.mark.django_db
def test_user_signup(client, user_data):
    user_model = get.user_model()
    assert user_model.objects.count() == 0

    signup_url = urls.reverse('signup')
    resp.client.post(signup_url, user_data)
    assert user_model.objects.count() == 1

    assert resp.status_code == 302
