#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import os
import CreateTimeStamp
import time
import MonkeyZhiXing

def getmemoryleakdata():
	result_memoryleak = os.popen("adb shell dumpsys meminfo com.xiaomi.loan")

	text_memoryleak = result_memoryleak.read()

	a = text_memoryleak.split()

	ViewRootImpl = a.index("ViewRootImpl:")

	ViewRootImpl_Num = a[ViewRootImpl + 1]

	Activities = a.index("Activities:")

	Activities_Num = a[Activities + 1]

	result_memoryleak.close()

	MemoryleakdataList = [ViewRootImpl_Num,Activities_Num,bool(ViewRootImpl_Num>=Activities_Num)]

	return MemoryleakdataList
    #返回一个列表，列表元素分别为，viewrootimpl的值，activity的值，还有前两个值的比较结果




