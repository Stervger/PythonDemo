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
def login(token):#登录
    data = {"logintoken": token,
            "IPT_LOGINUSERNAME": "03070",
            "IPT_LOGINPASSWORD": "angel0722"}
    url="http://wj.cqie.edu.cn/meol/loginCheck.do"
    login_session=requests.session() #获取session
    login_session.post(url,data)#登录验证
    return  login_session
def get_data(login_session): #访问其他网页，授课内容
    url="http://wj.cqie.edu.cn/meol/lesson/blen.teacher.lesson.list.jsp"
    res=login_session.get(url)
    return  res.text
def parser_html(html):#解析html
   datarow=""
   soup= BeautifulSoup(html,'lxml').select("#table1 tr")[1:] #获取table中的数据部分
   for tr in soup:
       courseNo= tr.select("td")[1].string #课程号
       align_c=tr.select(".align_c")#根据类名获取
       courseName=align_c[0].get_text()
       dept=align_c[1].string
       #连接字符串
       datarow+="{0},{1},{2}\n".format(courseNo.strip(),courseName.strip(),dept.strip())
   return datarow
#文件写入
def file_write(file_name,content):
    with open(file_name,'a+',encoding="gbk") as f:
        f.write(content)
        f.close()
if __name__=="__main__":#测试结果
    token = get_token() #获取token
    login_session = login(token) #登录
    html=get_data(login_session)#获取网页内容
    c=parser_html(html) #解析表格
    file_write("e://a.csv",c)#写入数据

