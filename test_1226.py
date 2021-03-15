# 伪装浏览器正规军
import urllib.request
import http.cookiejar


def savefile(data):
    save_path = 'C:\\Users\\gaofeng\\Documents\\Project\\output.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

def makemyopener(head={
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3508.0 Safari/537.36'
        }):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makemyopener()
uop = oper.open('http://www.sina.com')
data = uop.read()
print(data.decode())
savefile(data)