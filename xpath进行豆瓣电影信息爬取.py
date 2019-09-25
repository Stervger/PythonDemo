import requests
from lxml import etree
import time

#获取url并解析
url = 'https://movie.douban.com/subject/1292052/'
data = requests.get(url).text
s=etree.HTML(data)
#获取电影名称、导演、主演、时长信息
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
actor=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
time=s.xpath('//*[@id="info"]/span[13]/text()')

#以列表形式输出演员
ats = []
for a in actor:
    ats.append(a)

#显示获取的信息内容
print('name:',film)
print('director:',director)
print('actors:',ats)
print('duration:',time)
