import os
import pytest


@pytest.fixture(scope='session')
def resource_path(pytestconfig):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, 'tests/resources')


@pytest.fixture(scope='session')
def config_path(resource_path):
    return os.path.join(resource_path, 'test_config.json')
