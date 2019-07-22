from urllib import request,parse

if __name__=="__main__":
    qs={"kw":"李毅",
        "ie":"utf-8",
        "pn":0}
    urls = []
    #http: // tieba.baidu.com / f?ie = utf - 8 & kw = python & fr = search & red_tag = v0901067050
    baseurl = "http://tieba.baidu.com/f?"
    for i in range(10):
        pn = i*50
        qs["pn"] = str(pn)
        urls.append(baseurl+parse.urlencode(qs))
    print(urls)
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")
        print(url)
        print(html)
