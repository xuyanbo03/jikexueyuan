#coding=utf-8
import requests
import re

url='https://www.crowdfunder.com/browse/deals&template=false'

# html=requests.get(url).text
# print(html)

data={
    'entities_only':'true',
    'page':'1'
}
html_post=requests.post(url,data=data)
title=re.findall('"card-title">(.*?)</div>',html_post.text,re.S)
for each in title:
    print(each)