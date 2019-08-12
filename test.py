# -*- coding: utf-8 -*-
import re

print('hello world')
print(1)
print(2+3)
print(1.0)
print('hello')
print('hello'+'world')
print('hello'+"world")
print(1+2.0)
str1 = 'dd25p35x14'
#从开始匹配，匹配失败返回None，成功返回span对象
str2 = re.match('[a-z]+',str1)
print(str2.group(0))
#compile函数用于编译正则表达式,供match和search函数使用
patt = re.compile(r'[0-9]+')
#匹配所有，匹配失败返回None，成功返回匹配span对象
str3 = re.search('[0-9]+',str1)
print(str3.group(0))
#匹配加替换count=0表示匹配次，0代表匹配到结束，可以用函数替换
str4 = re.sub('[0-9]+','good',str1)
print(str4)
#把匹配内容放入列表
str5 = patt.findall(str1)
print(str5)
#匹配内容生成迭代器
str6 = re.finditer('[a-z]+',str1)
for i in str6:
    print(i.group())
#匹配的作为分割线进行分割
str7 = re.split('[a-z]+',str1)
print(str7)
#从键盘输入
str8 = input('请键入内容：')
print(str8)
