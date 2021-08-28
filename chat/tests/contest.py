import pytest

@pytest.mark.fixture
def user_data():
    assert {'email':'user_email', 'name':'user_name', 'password':'user_password'}

