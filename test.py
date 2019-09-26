import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import urllib.request
import urllib.parse
import re
import http.cookiejar
def getHtml(url):

    cj=http.cookiejar.CookieJar()

    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'),('Cookie’,‘VUID=B9CC5A50498B480385EF5FE50C23D6CF; UM_distinctid=1633e813a618ec-058c4f2c196519-3a614f0b-144000-1633e813a628a3; CNZZDATA3538029=cnzz_eid%3D243697563-1525759234-%26ntime%3D1525759234; Hm_lvt_49024937a7f937de669432245102dac6=1525762047,1525827929; Hm_lpvt_49024937a7f937de669432245102dac6=1525827929')]

    urllib.request.install_opener(opener)

    html_bytes = urllib.request.urlopen(url).read()

    html_string = html_bytes.decode( 'utf-8' )

    return html_string


html = getHtml("http://zst.aicai.com/ssq/openInfo/")

table = html[html.find('<table class=“fzTab nbt”>'):
            html.find('</table>')]

tmp = table.split('<tr \r\n\t\t                  onmouseout=',1)

trs = tmp[1]

tr = trs[: trs.find('</tr>')]

number = tr.split('<td   >')[1].split('</td>')[0]

print(number + '期开奖号码：',end='')

redtmp = tr.split('<td  class="redColor sz12" >')

reds = redtmp[1:len(redtmp)-1]#去掉第一个和最后一个没用的元素

for redstr in reds:

    print(redstr.split('</td>')[0] + ",",end='')

    print('蓝球：',end='')

blue = tr.split('<td  class="blueColor sz12" >')[1].split('</td>')[0]

print(blue)