#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import os

result = os.popen("adb devices")

text = result.read()

a = text.split()

b = []

j = 0

for i in a:
	j = j + 1
	if i == "device":
		c = a[j-2]
		b.append(c)
		print(a)
		if len(b) == 0:
			print("未识别设备，请刷新")
		if len(b) != 0:
			e = len(b)
			print("已获取%d台设备"%e)

result.close()