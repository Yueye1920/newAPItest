import pytest

# @pytest.mark.parametrize 固定标签，接受参数的名称
@pytest.mark.parametrize("input1,input2,expected", [(1, 2,3), (5, 5,10),(10,-2,8)])
def test_add(input1,input2,expected):
    assert input1 + input2 == expected