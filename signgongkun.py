#!/usr/bin/env python
# coding: utf-8

# In[11]:


import  requests
# from lxml import etree
import json

import os


# In[15]:


env=os.environ
# print(env)
passwd=env.get('gongkun_passwd')


# In[2]:


s = requests.session()
login_url='https://uis.nwpu.edu.cn/cas/login'
login_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",

                }
# {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
#             "Host":"uis.nwpu.edu.cn",
#             "Connection": "keep-alive",
#             "Content-Length":"165",
#             "Cache-Control": "max-age=0",
# #             "sec-ch-ua": ""Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99,
#             "sec-ch-ua-platform": "Windows",
#             "Content-Type": "application/x-www-form-urlencoded",
# #             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "Content-Type": "application/x-www-form-urlencoded",
#             "Origin": "https://uis.nwpu.edu.cn",
#             "Upgrade-Insecure-Requests": "1",
#             "Referer": "https://www.baidu.com/link?url=c1kkWysy-k9IwUHxfgs1v10pUI6I_uwyl67uWO0ka39ssJ0CTXET5SjFyHTAQB-0&wd=&eqid=8ff6c81d00104de800000006615d577a",
#             "Accept-Encoding": "gzip, deflate",
#             "Accept-Language": "zh-CN,zh;q=0.9",
#         }
login_data={
    '_eventId':"submit",
    'currentMenu':"1",
    'execution':"e1s1",
#     "geolocation":"",
    'password':passwd,
#     "submit":"=%E7%A8%8D%E7%AD%89%E7%89%87%E5%88%BB%E2%80%A6%E2%80%A6",
    'username':"2021264590"
}
# data={}

response = s.get(login_url,headers=login_headers)

login_response = s.post(login_url,headers=login_headers,data=login_data)
# print(login_response.text)
# print(login_response.text)
# print(s.cookies.get_dict())


# In[8]:


url = 'http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp'
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
#             "Host":"yqtb.nwpu.edu.cn",
#             "Connection": "keep-alive",
#             "Content-Length":"357",
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://yqtb.nwpu.edu.cn",
            "Referer": "http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp",
#             "Accept-Encoding": "gzip, deflate",
#             "Accept-Language": "zh-CN,zh;q=0.9",
#             "Cookie": "JSESSIONID=D93AA7828133C7B3FB6D3CA35B7FE1EE",
        }

body={
    "actionType":"addRbxx",
    "bdzt":"1",
    "glqk":"0",
    "sfjcqz":"0",
    "sfjcry":"0",
    "sfjkqk":"0",
    "sfjt":"0",
    "sfqz":"0",
    "sfyzz":"0",
    "szcsbm":"1",
    "szcsmc":"在学校",
    "tbly":"sso",
    "userLoginId":"2021264590",
    "userName":"龚坤",
    "userType":"2",
}
res=s.get('http://yqtb.nwpu.edu.cn/')
response = s.post(url,headers=headers,data=body)


# In[ ]:




