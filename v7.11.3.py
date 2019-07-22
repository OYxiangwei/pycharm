from urllib import request , parse
from http import cookiejar
import ssl
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler
https_handler = request.HTTPSHandler
opener = request.build_opener(cookie_handler,http_handler,https_handler)
ssl._create_default_https_context = ssl._create_unverified_context()
def login():
    login_url = "http://login.kaixin001.com/"
    data = {"email":"18275118695","password":"yxw@19890707"}
    data = parse.urlencode(data)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    req = request.Request(login_url,data=data.encode(),headers=headers)
    rsp = opener.open(req)
    html = rsp.read()
    html = html.decode()


def gethomepage():
    base_url = "http://www.kaixin001.com/home/?uid=181866690&s=97"
    rsp1 = opener.open(base_url)
    html = rsp1.read()
    html = html.decode()
    print(html)
if __name__=="__main__":
    login()
    gethomepage()