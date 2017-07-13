import requests
import re
import sys
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
html = requests.get('https://www.douyu.com/directory/game/DOTA2',headers = hea)
#html.encoding = 'utf-8'
#print(html.text)
web = re.findall('<img data-original=(.*?)src=',html.text,re.S)
# for each in web:
#     print(each)

if html.status_code == 200:
    x = 0
    with open('logo%s.jpg'%x, 'wb') as f:
        for chunk in html:
            f.write(chunk)