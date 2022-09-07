# coding=utf-8
"""
This must exists for py.tests to work out the path to 'ed' folder
"""

# 3rd party imports
import pytest

from src.docker_jinja3 import _local_env  # noqa F401


@pytest.fixture(autouse=True)
def reset_jinja(request):
    """
    Reset global _local_env variable between each tests to ensure clean state
    """
    global _local_env

    _local_env = {"global": {}, "filters": {}}
