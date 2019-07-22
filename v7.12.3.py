import requests
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

rsp = requests.get(url,headers=headers)
html = rsp.text
#print(html)
html = etree.HTML(html)
rst = html.xpath('//div[@class="recmd-content"]')
print(rst)
for r in rst:
    print(r.text)