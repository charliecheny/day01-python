
import requests
import re
# 获取小说列表
def get_novel_list():
    response = requests.get('http://www.quanshuwang.com/list/1_1.html')
    response.encoding = 'gbk'
    reg = r'<a target="_blank" href="(.*?)" class="l mr10"'
    html = response.text
    return re.findall(reg,html)

# 获取章节列表
def get_chapter_list(novel_url):
    response = requests.get(novel_url)
    response.encoding = 'gbk'
    reg = r'<a href="(.*?)" class="reader"'
    html = response.text

    chapter_list_url = re.findall(reg, html)[0]
    response = requests.get(chapter_list_url)
    response.encoding = 'gbk'
    html = response.text
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    return re.findall(reg,html)

# 获取小说内容
def get_chapter_content(chapter_url):
    response = requests.get(chapter_url)
    response.encoding = 'gbk'
    html = response.text
    # .* 表示匹配任意字符不换行 字符串里有()在正则里都会被识别,需要被转义
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    content = re.findall(reg,html,re.S)
    if content:
        content = content[0]
    else:
        content = ''
    return content


for novel_url in get_novel_list():
    for chapter_url,chapter_name in get_chapter_list(novel_url):
        chapter_content = get_chapter_content(chapter_url)
        # 保存文件
        fn = open(chapter_name+'.html',mode='w')
        fn.write(chapter_content)
        fn.close()
        # break # 只爬了一个章节
        # 取数据第二种方式
        # chapter_url = i[0]
        # chapter_name = i[1]
    break # 不需要每本小说都打开