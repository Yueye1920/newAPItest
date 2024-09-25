import json
import os
import pdb

import allure
import pytest
import requests
from common.methodclass import methodcs
from common.fileData import FileReader
from common.loggerController import Logger

logs = Logger()
class TestCase:
# 读取数据

    AllCaseData= FileReader.readExcelToDict()
    ff= methodcs()

    def __dynmic_title(self,CaseData):

        # 动态生成标题
        if CaseData["caseName"] is not None:
            casename = "ID({})-({})".format(CaseData["id"], CaseData["caseName"])
            allure.dynamic.title(casename)
            # allure.dynamic.title(CaseData["casename"])

        # # 动态获取story模块名
        # if CaseData["storyName"] is not None:
        #     allure.dynamic.story(CaseData["storyName"])
        #
        # # 动态获取feature模块名
        # if CaseData["featureName"] is not None:
        #     allure.dynamic.feature(CaseData["featureName"])
        #
        # # 动态获取备注信息
        # if CaseData["remarkName"] is not None:
        #     allure.dynamic.description(CaseData["remarkName"])

    @pytest.mark.parametrize("CaseData",AllCaseData)
    def testData(self,CaseData):

        # 调用动态生成标题
        self.__dynmic_title(CaseData)

        row=CaseData["id"]
        col=9
        logcol=10

        # print(CaseData["url"])
        # print(CaseData["method"])
        # print(CaseData["headers"])
        # print(CaseData["datas"])
        # print(type(CaseData["datas"]))
        # print(type(eval(CaseData["datas"])))

        # 方法一：参数一一对应
        # url= CaseData['url']
        # method =CaseData['method']
        # headers=eval(CaseData['headers'])  # 将str转换为dict （json格式用dict）
        # datas=eval(CaseData['datas'])  # 将str转换为dict （json格式用dict）
        # response = requests.post(url=url, data=datas, headers=headers)
        # print(response.text)

        try:
        # 方法二：用字典，将数据封装(请求的数据)
            dict_data={
                "url" : CaseData['url'],
                "headers" : eval(CaseData['headers']),    # 将str转换为dict （json格式用dict）
                "data" : CaseData['datas']     # 将str转换为dict （json格式用dict）
            }
            self.url=dict_data["url"]
            self.headers = dict_data["headers"]
            self.data=dict_data["data"]
            # logs.Logger.info("请求参数为：{}，{}，{}".format(self.url,self.headers,self.data ))
            # print(dict_data)
        except  Exception:
            print("数据解析错误")
            FileReader.writeExcelToDict(row=row,column=col,value="数据解析错误")
        # res = methodcs.post(**dict_data)  # 用**解包
        # print(res.text)
        else:
        # 方法三：用反射
            method =CaseData['method']
            # res = getattr(self.ff, method)(**dict_data)
            try:
                res = getattr(self.ff,method)(**dict_data)
                # print(res)
                if res is not None:
                    value=res.text
                    FileReader.writeExcelToDict(row=row, column=logcol, value=value)
                else:
                    value = "日志为空，数据提取失败，请检查参数"
                    FileReader.writeExcelToDict(row=row, column=logcol, value=value)
            except Exception:
                print( "请求失败")
                value="请求失败"
                FileReader.writeExcelToDict(row=row, column=logcol, value=value)


            # print(res.text)
            # FileReader.writeExcelToDict(row=row, column=col, value="执行成功")
            # return res.text

            try:
                msg=self.ff.get_text(res.text,CaseData['actualResult'])
                # logs.Logger.info("返回结果为：{}".format(msg))
                # print(msg)
            except Exception:
                # value=res.text
                # FileReader.writeExcelToDict(row=row, column=col, value=value)
                # print("数据错误")
                if res is not None:
                    value = "数据提取失败，请检查参数"
                    FileReader.writeExcelToDict(row=row, column=col, value=value)
                else:
                    value = "数据提取失败，请检查参数"
                    FileReader.writeExcelToDict(row=row, column=col, value=value)

            else:
                if CaseData['expectResult'] ==msg:
                    value = "执行通过"
                    print("成功")
                    FileReader.writeExcelToDict(row=row, column=col, value=value)
                else:
                    value = "执行失败"
                    print("失败")
                    FileReader.writeExcelToDict(row=row, column=col, value=value)
            #
                # finally:
                #     assert CaseData['expectResult']==msg

            logs.logger.info("请求参数：{}，{}，{}".format(self.url,self.headers,self.data ))
            if res is not None:
                logs.logger.info("返回结果：{}".format(res.text))
            else:
                value="无响应数据"
                logs.logger.info("返回结果：{}".format(value))




if __name__ == "__main__":
    # pytest.main()
    pytest.main(["-vs","test_excel.py","--alluredir","D:/dome/newapitest/newApitest/allure-results/","--clean-alluredir"])
    os.system("allure generate allure-results -o allure-reports/ --clean")
