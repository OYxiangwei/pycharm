from urllib import request , parse

proxy_list = [
    {"http":'120.83.105.47:9999'},
    {"http":'222.89.32.147:9999'},
    {"http":'114.230.117.96:9999'}
]
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)
#request.install_opener(opener)
import random
url = "http://www.baidu.com"
try:
    opener = random.choice(opener_list)
    request.install_opener(opener)
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except Exception as e:
    print(e)