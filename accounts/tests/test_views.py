from django.test import TestCase
from django.urls import path
from django import urls

import pytest

from mytests.controllers import test_render_views_

@pytest.mark.parametrize(param, [
    ('chatroom'),
    ('index'),
    ('base')
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp     = client.get(temp_url)
    return resp.status_code == 200
