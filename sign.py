#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  requests
from lxml import etree
import json


# In[2]:


url = 'http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp'
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
            "Host":"yqtb.nwpu.edu.cn",
            "Connection": "keep-alive",
            "Content-Length":"357",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://yqtb.nwpu.edu.cn",
            "Referer": "http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "JSESSIONID=D93AA7828133C7B3FB6D3CA35B7FE1EE",
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
    "userLoginId":"2021264575",
    "userName":"成泳甫",
    "userType":"2",
}



# In[3]:


response = requests.post(url,headers=headers,data=body)


# In[4]:


print(response.text)


# In[ ]:




