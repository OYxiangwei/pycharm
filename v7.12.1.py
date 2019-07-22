from urllib import parse,request,error
from http import cookiejar
import ssl

def log_in():
    log_url ="https://security.kaixin001.com/login/login_auth.php"
    data = {
            'email':'18275118695',
            'password':'yxw@19890707'}
    data = parse.urlencode(data).encode()
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
             'Content-Length': len(data)}
    f = r'kaixin.txt'
    #ssl._create_default_https_context = ssl._create_unverified_context()
    cookie_handler = cookiejar.MozillaCookieJar(f)
    http_handler = request.HTTPCookieProcessor(cookie_handler)
    opener = request.build_opener(http_handler)
    req = request.Request(log_url,data=data,headers=headers)
    try:
        rsp = opener.open(req)
        cookie_handler.save(f,ignore_discard=True,ignore_expires=True)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
if __name__=="__main__":
    log_in()