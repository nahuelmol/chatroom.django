[pytest]
DJANGO_SETTINGS_MODULE = chatroom.settings
addopts = -v -s --cov=chat/tests/ no-cov-on-fail
