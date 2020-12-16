# 附加题
# 这一次, 我们考验的是工程能力
# 这是我们 Minieye 的招聘网站: https://www.minieye.cc/career
# 请获取我们公司当前招聘的职位信息
# 输出文件:  Minieye招聘信息.csv
# 输出格式:  职位名称	职位类别	工作城市	工作年限	申请职位
import requests
from jsonpath import jsonpath
import json
import xlwt

def get_data():
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    url = "https://www.minieye.cc/api/all_position?"
    r = requests.get(url,headers=head)
    r.encoding = r.apparent_encoding
    html = r.text
    html_json = json.loads(html)
    names = jsonpath(html_json, "$..name")
    types = jsonpath(html_json, "$..type")
    citys = jsonpath(html_json, "$..city")
    workYears = jsonpath(html_json, "$..workYear")
    descriptions = jsonpath(html_json, "$..description")
    info = []
    for name,type,city,workYear,description in zip(names,types,citys,workYears,descriptions):
        career = [name,type,city,workYear,description]
        info.append(career)
    return info

def savedate(info):

    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet("Minieye_Crawl",cell_overwrite_ok=True)
    col = ("职位名称","职位类别","工作城市","工作年限","申请职位")
    for i in range(0, 5):
        sheet.write(0, i, col[i])  # 创建5个索引
    for i in range(0,len(info)):
        print("第%d条" % (i + 1))
        data = info[i]  # 获取一个职位的信息
        for j in range(0, 5):
            sheet.write(i + 1, j, data[j])  # 写入一个职位的信息
    book.save("Minieye招聘信息.csv")



if __name__ == '__main__':
    info = get_data()
    savedate(info)


