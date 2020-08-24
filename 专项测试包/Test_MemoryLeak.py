#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import MonkeyZhiXing
import JudgeMonkeyStatus
import MemoryLeakFunction
import time

MonkeyZhiXing.Memory_Leak_Monkey()

time.sleep(10)

while JudgeMonkeyStatus.judgemonkeystatus():
 	time.sleep(10)

ResultList = MemoryLeakFunction.getmemoryleakdata()

if ResultList[2] == True:
	print("内存未泄漏，ViewRootImpl的值为%s,Activity的值为%s,测试结果通过"%(ResultList[0],ResultList[1]))
else:
	print("内存发生泄漏，ViewRootImpl的值为%s,Activity的值为%s"%(ResultList[0],ResultList[1]))




