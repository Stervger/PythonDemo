import requests
from bs4 import BeautifulSoup
def get_token():#获取token
  url="http://wj.cqie.edu.cn/meol/homepage/common/"
  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
  #获取html页面内容
  html=requests.get(url,headers=headers).text
  bs=BeautifulSoup(html,"lxml")
  #获取标签<input type = "hidden" name = "logintoken" value = "1551074505872" >
  token=bs.select("input[name=logintoken]")
  return token[0].attrs["value"]#返回解析出的value
def login(token):#登录验证
    data = {"logintoken": token,
            "IPT_LOGINUSERNAME": "用户名",
            "IPT_LOGINPASSWORD": "密码"}
    url="http://wj.cqie.edu.cn/meol/loginCheck.do"
    login_session=requests.session()
    login_session.post(url,data)#发送登录请求
    return  login_session
def get_html(login_session):
    url=" http://wj.cqie.edu.cn/meol/lesson/blen.teacher.lesson.list.jsp"
    r=login_session.get(url)
    print(r.text)
if __name__=="__main__":#运行测试
    token = get_token() #获取token
    r = login(token) #登录
    print(get_html(r))






