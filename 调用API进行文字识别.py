# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:59:24 2017

@author: Lesile
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
import json


os.getcwd()
os.chdir("C:\\Users\\Lesile\\Desktop")
URL = r"https://api-cn.faceplusplus.com/imagepp/v1/recognizetext"
CONST_KEY = r'u8LbxLj-7RAH4P_nax11goWTgRTtukOj'
CONST_SECRET = r'Fi6SkAt2EgDb_cAixPAeoI73__qxbYto'


multiple_files = [
	('image_file', ('save.png', open('save.png', 'rb'), 'image/png')),
]


data = (('api_key', CONST_KEY), ('api_secret', CONST_SECRET))

r = requests.post(URL, files = multiple_files, data = data)

print(r.text)

text = r.text

data=json.loads(text)  

result = data["result"]

##方式一：直接提取textline
b = result[0]
c = b["value"]

finalresult = [i["value"] for i in result]
print(finalresult)

##方式二：自己拼接
b = result[0]
c = b["child-objects"]
d = c[0]

c = b["value"]