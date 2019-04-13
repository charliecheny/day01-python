
# 第一步 导入第三方资源
import requests # http请求库，用于请求网络资源
import lxml.html # 用户处理pyhthon语言中的xml html
import csv # 可以导入导出数据的格式 或者载体
# 第二步 获取目标网站
# https://movie.douban.com/top250?start=0&filter=  第一页
# https://movie.douban.com/top250?start=25&filter= 第二页
# https://movie.douban.com/top250?start=50&filter= 第三页
# https://movie.douban.com/top250?start=75&filter= 第四页
# https://movie.douban.com/top250?start=100&filter= 第五页
# 规律
doubanUrl = 'https://movie.douban.com/top250?start={}&filter='
# 第三步 解析目标网站    通过开发者工具人为的找一遍  通过网页源代码 ---> class = info(标签)
# 定义一个函数 目的:获得网页数据、文本
def getSource(url):

    response = requests.get(url)
    # 修改编码格式 防止出现乱码
    response.encoding = 'utf-8'
    # 返回一个网页源代码
    return response.text

# 定义第二个函数 目的:获取class = info数据 每一个电影信息  标题 引言 地址
def getEveryItem(source):
    # 定义一个处理xml的对象
    selector = lxml.html.document_fromstring(source)

    # 通过Xpath技术来找到 class = info 列表对象  Ctrl+U 查看网页源代码 Ctrl+F 搜索标签
    movieItemList = selector.xpath('//div[@class="info"]')

    # 定义一个列表 目的:展示数据 [{},{},{},{},{}......]
    movieList = []

    # 找每一个电影的信息 标题 引言 地址
    for eachMovie in movieItemList:

        # 定义一个字典 目的:保存数据
        movieDict = {}
        title = eachMovie.xpath('div[@class="hd"]/a/span[@class="title"]/text()')# 标题
        otherTitle = eachMovie.xpath('div[@class="hd"]/a/span[@class="other"]/text()')# 副标题
        link = eachMovie.xpath('div[@class="hd"]/a/@href')[0]# url
        star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]# 评分
        quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')# 引言
        # 解决了有的电影引言W为空的现象
        if quote:
            quote = quote[0]
        else:
            quote = ''
        # 保存到字典当中
        movieDict['Title'] = ''.join(title + otherTitle)
        movieDict['url'] = link
        movieDict['star'] = star
        movieDict['quote'] = quote

        print(movieDict)

        movieList.append(movieDict)
    return movieList

# 第四步 下载数据
# 定义第三个函数
def writeData(movieList):
    with open('Douban.csv','w',encoding='utf-8',newline='') as ft:
        writer = csv.DictWriter(ft, fieldnames=['Title', 'star', 'quote', 'url'],dialect='excel')
        writer.writeheader() # 写入表头
        for each in movieList:
            writer.writerow(each)


# 启动程序
if __name__ == '__main__':
    movieList = []

    for i in range(10):
        # 获取url
        pageLink = doubanUrl.format(i * 25)
        print(pageLink)

        # 有了url 我们就可以获取网页数据
        source = getSource(pageLink)
        # 有了源代码 我们就可以获得电影信息
        movieList += getEveryItem(source)

    print(movieList[:10])
    writeData(movieList)

















