# 用Python抓取指定页面
import urllib.request


url = "http://www.baidu.com"
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# print(data)

a = urllib.request.urlopen(url)
# type(a)
geturl = a.geturl()
info = a.info()
getcode = a.getcode()

# print(geturl)
# print(info)
# print(getcode)


# 用Python简单处理URL
import urllib
import urllib.request


data = {}
data['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)