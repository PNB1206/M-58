import pytest

""" This is parent class of all test classess"""


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass