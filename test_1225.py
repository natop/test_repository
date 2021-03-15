# Python的队列
from collections import deque


queue = deque(["Eric", "Johon", "Machiael"])
queue.append("Terry")   #Terry入队
queue.append("Graham")  #Graham入队
print(queue.popleft())  # 队首元素出队 输出: 'Eric'
print(queue.popleft())  # 队首元素出队 输出: 'John'
print(queue)

# Python的集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # 这里演示的是去重功能

print('orange' in basket)   # 快速判断元素是否在集合内
print('crabgrass' in basket)

# 下面展示两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)    # 集合a中包含元素
print(a | b)    # 集合a或b中包含的所有元素
print(a & b)    # 集合a和b中都包含了的元素
print(a ^ b)    # 不同时包含于a和b的元素

# Python网络爬虫Ver 1.0 alpha
import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()
url = 'https://finance.sina.com.cn/stock/'

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    visited |= {url}
    print('已经抓取：' + str(cnt) + '正在抓取 <--- ' + url)
    cnt += 1
    urlop = urllib.request.urlopen(url)
    if 'html' not in urlop.getheader('Content-Type'):
        continue
# 避免程序异常中止, 用try..catch处理异常
    try:
        data = urlop.read().decode('utf-8')
    except:
        continue
# 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 ---> ' + x)