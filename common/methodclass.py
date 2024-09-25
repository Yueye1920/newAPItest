import json

import requests
import jsonpath


class methodcs:

    def get(self,url,params=None,headers=None,**kwargs):
        print("当前是get方法")
        # return requests.get(url, data=params, headers=headers, **kwargs)
        try:
            return requests.get(url,data=params,headers=headers,**kwargs)
        except Exception :
            print("请求方法错误")

    def post(self,url,data=None,headers=None,**kwargs):
        print("当前是post方法")
        return requests.post(url,data=data,headers=headers,**kwargs)

    def get_text(self, response, key):
        if isinstance(response,str):
            response=json.loads(response)
        value_list =jsonpath.jsonpath(response,key)
        return value_list[0]


if __name__ == '__main__':
    methods= methodcs()

# # getattr(实例化对象名,"名称")
# print(getattr(methods,"get"))
# print(getattr(methods,"post"))


