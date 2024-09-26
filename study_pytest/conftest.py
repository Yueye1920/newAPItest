import pytest


"""
@pytest.fixture 用于自定义测试用例的前置步骤
"""
@pytest.fixture
def setup_data():
    return [1,2,3,4,5]