# 附加题
# 这一次, 我们考验的是工程能力
# 这是我们 Minieye 的招聘网站: https://www.minieye.cc/career
# 请获取我们公司当前招聘的职位信息
# 输出文件:  Minieye招聘信息.csv
# 输出格式:  职位名称	职位类别	工作城市	工作年限	申请职位

from bs4 import BeautifulSoup
import requests

source_list = []
headers = {
    'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/63.0.3239.132 Safari/537.36'
}
url ='https://www.minieye.cc/career'
lis1 = []


html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'lxml')
row = soup.select('.position-table > thead > tr > td')


for i in row:
    lis1.append(i.text.strip())

print(lis1)

# 感谢这次笔试考核，让我明白自己要学的还有很多，谢谢！