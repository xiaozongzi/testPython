import re
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


html = getHtml(
    "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1505296218372_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1505296218373%5E00_712X834&word=image")
html = html.decode('utf-8')
reg = r'src="(.*?\.jpg)"'
imgre = re.compile(reg)
imglist = re.findall(imgre, html)
print(len(imglist))
for each in imglist:
    print(each.count(".jpg"))

