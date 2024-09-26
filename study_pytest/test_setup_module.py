def setup_module():
    print("文件的前置操作")

def teardown_module():
    print("文件的后置操作")

def test_example1():
    print("执行测试用例1")

def test_example2():
    print("执行测试用例2")

def setup_function():
    print("执行函数级别前置操作")

def teardown_function():
    print("执行函数级别后置操作")