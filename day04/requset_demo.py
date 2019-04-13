import re
import requests,chardet
if __name__ == '__main__':

    url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip&oq=ip&rsv_pq=860ef55b0001fa05&rsv_t=e0b5illF5YYxR7cD%2BymdJYdqlMvU4zb7ydUtM0YAlnOOfxWxw3eBYRg8s%2FQ&rqlang=cn&rsv_enter=0"
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    ambition=requests.get(url,headers=headers)
    print(ambition.text)
    ambition.encoding=chardet.detect(ambition.content)['encoding']
    html=ambition.text
    paa='<span class="c-gap-right">本机IP: (.*)</span>'
    ip=re.findall(paa,html)
    ipa=''.join(ip)
    print('本地ip：'+ipa)
    with open('ip.txt', 'w') as f:
        f.write(ipa)
    with open('ip.txt', 'r') as f:
        print(f.read())
