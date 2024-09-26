import pytest

# 指定fixture的作用域为测试模块，只执行一次
@pytest.fixture(scope="module")
def setup_module():
    print('setup module')

# 指定fixture的作用域为测试函数，每个函数前执行一次
# @pytest.fixture(scope="function")
# def setup_module():
#     print('function module')

# 参数化fixture
@pytest.fixture(params=[1, 2, 3,4])
def setup_data(request):
    print(f"setup data:{request.param}")
    return request.param

# 自动使用fixture,fixture也能实现前置和后置
@pytest.fixture(autouse=True)
def setup_autouse():
    print("autouse fixture")


# 自定义fixture名称
@pytest.fixture(name="custom_fixture")
def setup_custom():
    print("custom fixture")

# 测试函数使用fixture
def test_example(setup_module,setup_data,custom_fixture):
    print(f"test example:{setup_data}")