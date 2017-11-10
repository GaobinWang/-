#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 01:56:45 2017

@author: Lesile
"""

###加载库
import os
import requests
import json
import numpy as np
import pandas as pd


###设置全局变量
file_path = "E:\\Github\\RecognizeText" #默认工作路径
os.chdir(file_path) 
image_name = 'example1.png' #需要识别的图片的名称
URL = r"https://api-cn.faceplusplus.com/imagepp/v1/recognizetext"  #Recognize Text API的URL 
CONST_KEY = r'u8LbxLj-7RAH4P_nax11goWTgRTtukOj'  #调用 Recognize Text API的API Key
CONST_SECRET = r'Fi6SkAt2EgDb_cAixPAeoI73__qxbYto' #调用 Recognize Text API的API Secret

###向Recognize Text API输入请求参数，并获取返回值
multiple_files = [
	('image_file', (image_name, open(image_name, 'rb'), 'image/png')),
]

data = (('api_key', CONST_KEY), ('api_secret', CONST_SECRET))
r = requests.post(URL, files = multiple_files, data = data)
text = r.text
print(text)


###对返回值进行解析
result=json.loads(text) #将返回的字符串转化为字典
result.keys() #查看字典的键，其中result代表转换后的结果
result = result["result"] #提取转换后的文字

"""
##解析方式一：直接提取textline
b = result[0]
c = b["value"]
finalresult = [i["value"] for i in result]
print(finalresult)
"""

##解析方式二：根据坐标进行拼接
res = []
for i in range(len(result)):
    a = result[i] #获取每一个子块的内容
    b = a["child-objects"] #获取子块中每一个文字的列表
    for j in range(len(b)):
        c = b[j] #获取每一个字体的位置，值
        positions = c['position']
        position_x = np.mean([i['x'] for i in positions]) #改字体沿着x轴的中点
        position_y = np.mean([i['y'] for i in positions]) #改字体沿着y轴的中点
        value = c['value']
        arr = [position_x,position_y,value]
        res.append(arr)
        
res = pd.DataFrame(res,columns = ['x','y','value']) 
res.sort_values(by = ['y'])
