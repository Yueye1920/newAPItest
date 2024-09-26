class TestClass(object):
    @classmethod
    def setup_class(cls):
        print("类的前置操作")

    @classmethod
    def teardown_class(cls):
        print("类的后置操作")

    def test_example3(self):
        print("执行测试用例1")

    def test_example4(self):
        print("执行测试用例2")

    def setup_function(self):
        print("执行函数级别前置操作")

    def teardown_function(self):
        print("执行函数级别后置操作")