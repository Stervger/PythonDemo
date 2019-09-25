from urllib import request,parse

# url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

# resp = request.urlopen(url)
# print(resp.read())

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}

data = {
    'first':'true',
    'pb':1,
    'kd':'python'
}
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode("utf-8"),method='post')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))