# 发送请求
import requests
# response = requests.get('http://httpbin.org/get', headers=)
# # 获取返回的html信息
# response.encoding = 'utf-8'
# print(response.text)
#
# print(response.headers)
# # 请求状态码
# print(response.status_code)
# # 获取网页的二进制内容
# print(response.content)
# print(response.url) # 获取请求的url
# print(response.cookies) # 获取cookie

# # 还可以添加请求头进行请求
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
# response = requests.get('http://httpbin.org/get', headers=headers )
# print(response.headers)
# print(response.text)

# # 带参数的get请求
# data = {"name": "fanchao", "passport": "123456"}
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)

# # 带参数的post请求
# data = {"name": "fanchao", "passport": "123456"}
# response = requests.post('http://httpbin.org/post', data=data)
# print(response.text)

# 从网上读取二进制数据，比如图片
response = requests.get('https://www.baidu.com/img/bd_logo1.png', headers=headers)
# 这个是直接获取字节码，这个是要保存的文件
print(response.content)
# 这个是获取解码后的返回内容，这个是乱码
print(response.text)
# 用文件来把图片下载下来
with open('baidu.png', 'wb') as f: # 注意写的方式是以二进制方式写入
 f.write(response.content)
 print('下载完毕')