#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import os
import CreateTimeStamp
import time

def getBootTimeData():
	os.popen("adb shell am force-stop com.xiaomi.loan")

	time.sleep(5)

	result_boottime = os.popen("adb shell am start -W com.xiaomi.loan/com.xiaomi.jr.app.MiFinanceActivity")

	text_boottime = result_boottime.read()

	a = text_boottime.split()

	BootTimeSituation = a.index("TotalTime:")

	BootTimeData = a[BootTimeSituation + 1]

	result_boottime.close()

	BootTimeDataList = [BootTimeData, bool(int(BootTimeData) <= 400)]

	return BootTimeDataList