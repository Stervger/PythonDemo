#encoding: utf-8
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
}

# 1、网页抓取cookie
# dapeng_url = "http://www.renren.com/880151247/profile"
#
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
#     "Cookie":'anonymid=k10s58muhb0u82; depovince=CQ; jebecookies=4f2aea6a-16cc-49db-a5d6-1b1f692b5702|||||; _r01_=1; JSESSIONID=abc7rArkWI8LHauBw7T1w; ick_login=7579cdd9-3931-4dcd-9ed2-3b5ea8db00c6; t=f2054d37e3b5d9213e40feee6d3f796e1; societyguester=f2054d37e3b5d9213e40feee6d3f796e1; id=972340571; xnsid=920f985e; ver=7.0; loginfrom=null; springskin=set; jebe_key=debe3c98-9549-4d30-9f42-9ddd09825791%7C9ecdb6e70e24ce488f725c752159e0c4%7C1569507536444%7C1%7C1569507538897; jebe_key=debe3c98-9549-4d30-9f42-9ddd09825791%7C9ecdb6e70e24ce488f725c752159e0c4%7C1569507536444%7C1%7C1569507538899; vip=1; wp_fold=0'
# }
# req = request.Request(url=dapeng_url,headers=headers)
# resp = request.urlopen(req)
# with open('renren.html','w',encoding='utf-8') as fp:
#     #write必须写入一个str数据类型
#     #resp.read()读出来的是一个bytes类型
#     #bytes -> decode -> str
#     #str -> encode-> bytess
#     fp.write(resp.read().decode('utf-8'))

# 2、爬虫自动登录

def get_opener():
    # 1、登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    # 1.4 使用opener发送登录的请求（邮箱和密码）
    data = {
        'email': '17774992917',
        'password': 'wjh1186806272'
    }
    log_url = "http://www.renren.com/PLogin.do"
    req = request.Request(log_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)


def visit_profile(opener):
    # 2、访问个人主页
    dapeng_url = "http://www.renren.com/880151247/profile"
    # 获取个人主页的时候不要新建一个opener，使用之前已经包含了登录所需cookie信息的opener
    req = request.Request(dapeng_url, headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)