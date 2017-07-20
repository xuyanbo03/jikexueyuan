# coding=utf-8
import re
import requests

f = open('source.txt', 'rb')
html = f.read().decode('utf-8')
f.close()

pic_url = re.findall('img src="(.*?)"', html, re.S)
i = 0
for each in pic_url:
    print("now downloading:" + each)
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.png', 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
