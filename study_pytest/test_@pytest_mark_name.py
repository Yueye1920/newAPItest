import pytest

"""
@pytest.mark.login
@pytest.mark.name 用于过滤对应标签的测试用例
"""

@pytest.mark.login
def test_login():
    print("用户登陆")


@pytest.mark.case_a
def test_case_a():
    print("执行用例a")


@pytest.mark.case_b
def test_case_b():
    print("执行用例b")


@pytest.mark.quit
def test_quit():
    print("用户退出")

