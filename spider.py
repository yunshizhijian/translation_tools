# -*- coding:utf-8 -*-
import requests
import os
url= 'https://fanyi.baidu.com/v2transapi' #网址
#访问网址
#模拟浏览器
print("请输入你想翻译的语言")
translat_Word= input()
if(translat_Word):
    word = input("请输入你想翻译的英语\n")
    data = {
        'from': 'en',
        'to': 'zh',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': 3
    }
response = requests.post(url, data=data)
data = response.json()

means = data['dict_result']['simple_means']['symbols'][0]['parts']
#创建文件夹
if not os.path.exists("my_%s" % word):
    os.makedirs("my_%s" % word)
dir_name = "my_%s" % word

#用一个text文件保存,文件名用单词名字
'''
flie_handler = open('%s.txt'%word,'w',encoding='utf-8')
for item in means:
    flie_handler.write(item['part'] + ' '.join(item['means']) +'\n')
flie_handler.close()
with可以省略open
'''
mp3_url = 'https://fanyi.baidu.com/gettts?lan=en&text=%s&spd=3&source=web' %word
mp3_response = requests.get(mp3_url)
mp3_data = mp3_response.content #二进制 字节数据
with open('%s/%s.mp3'%(dir_name, word), 'wb') as f:
    f.write(mp3_data)
with open('%s/%s.txt'%(dir_name,word),'w',encoding='utf-8') as f:
    for item in means:
     f.write(item['part'] + ' '.join(item['means']) +'\n')