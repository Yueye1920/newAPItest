import os

import pytest
import allure

if __name__ == "__main__":
    pytest.main()


# 切换路径
# cd D:\dome\newapitest\newApitest\testcase
# 执行测试用例
# pytest test_excel.py --alluredir ./allure-results/
# 生成报告
# allure generate allure-results -o allure-reports/ --clean
# 打开报告
# allure open allure-reports/