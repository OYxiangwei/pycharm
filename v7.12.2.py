from urllib import request

url = "https://maoyan.com/board"
rsp = request.urlopen(url)
html = rsp.read().decode()
#print(html)
import re
pattern = re.compile(r"<dd>(.*?)</dd>",re.S)
movies = pattern.findall(html)
print(len(movies))

for movie in movies:
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(movie)[1]
    print(title)