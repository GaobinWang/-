# 通用文字识别（RecognizeText）

本项目主要介绍以下内容：

* 如何调用faceplusplus（旷视科技）的人工智能开放平台API接口进行通用文字识别

* 如何利用"汉王OCR"软件进行通用文字识别

----

## 旷视科技Recognize Text API的使用

旷视科技为人工智能领域的优秀企业，支付宝的人脸识别技术由其提供。Recognize Text API为旷世科技提供的通用文字识别API，更多的应用可参考网址：https://console.faceplusplus.com.cn/dashboard

### 准备材料

* API Key

登录旷视科技网站，注册账号，并创建API Key。具体过程可参考网页：https://console.faceplusplus.com.cn/documents/5671787

* Python 3.x

建议直接安装Anaconda，下载地址为：https://www.anaconda.com/download/

### Recognize Text API的使用说明

Recognize Text API可以通过POST调用，在Shell中使用curl，在Chrome中可以使用Postman插件，在python中我们可以使用requests库中的post方法。接下来，我们主要介绍如何利用Python调用Recognize Text API。

关于Recognize Text API的使用，具体可参考网址：https://console.faceplusplus.com.cn/documents/7776484


* **描述**

调用者提供图片文件或者图片URL，进行图片分析，找出图片中出现的文字信息。


* **图片要求：**

图片格式：JPG(JPEG)，PNG

图片像素尺寸：最小48*48像素，最大800*800像素

图片文件大小：2MB


* **调用URL**

https://api-cn.faceplusplus.com/imagepp/v1/recognizetext

* **调用方法**

POST

* **权限**

所有 API Key 都可以调用本 API。

* **请求参数**

|是否必选|参数名|类型|参数说明
|--------|--------|----|-----
|必选|api_key|String|调用此API的API Key
|必选|api_secret|String|调用此API的API Secret
|必选（三选一）|image_url|String|图片的URL 
|               |image_file |File|一个图片，二进制文件，需要用post multipart/form-data的方式上传。
|               |image_base64	|String	|base64编码的二进制图片数据如果同时传入了image_url、image_file和image_base64参数，本API使用顺序为image_file优先，image_url最低。

其他参数可参考网址：https://console.faceplusplus.com.cn/documents/7776484

### 利用Python调用Recognize Text API的步骤

* Step1:通过Python中requests库的post方法向Recognize Text API的URL传递三个参数：api_key、api_secret、image_file，并获取返回结果

* Step2:对返回结果进行解析，以获取识别后的文本

具体实现可参考文件：调用API进行文字识别.py


## 汉王OCR的使用

参考Word文档：汉王OCR的使用



