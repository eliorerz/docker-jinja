# coding=utf-8
"""
This must exists for py.tests to work out the path to 'ed' folder
"""

# djinja package imports

# 3rd party imports
import pytest


@pytest.fixture(autouse=True)
def reset_jinja(request):
    """
    Reset global _local_env variable between each tests to ensure clean state
    """
    global _local_env

    _local_env = {
        "global": {},
        "filters": {}
    }
