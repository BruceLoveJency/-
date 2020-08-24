#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮
import time
import CreateTimeStamp
import os

def judgemonkeystatus():
	result_monkey = os.popen("adb shell \" ps | grep monkey \" ")
	text_monkey = result_monkey.read()
	if len(text_monkey) == 0:
		print("monkey测试已结束，log已输出")
		result_monkey.close()
		return False
	else:
		print("monkey还在继续，当前时间为%d"%CreateTimeStamp.gettimestamp())
		return  True
	result_monkey.close()