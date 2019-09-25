from urllib import request
import time

#未使用代理
# url = 'http://www.httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

#使用代理
url = 'http://www.httpbin.org/ip'
#1、使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({"http":"125.110.109.87:9000"})
#2、使用handler构建一个opener
opener = request.build_opener(handler)
#3、使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())

time.sleep(10)