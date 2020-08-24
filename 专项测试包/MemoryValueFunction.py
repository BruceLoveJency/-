#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import os
import time

def InitializeAppStatus():
	os.popen("adb reboot")

	time.sleep(60)

	os.popen("adb shell input swipe 540 1300 540 500 100")



def GetOnActivityMemoryValue():
	# os.popen("adb reboot")
	#
	# time.sleep(60)

	os.popen("adb shell am start -W com.xiaomi.loan/com.xiaomi.jr.app.MiFinanceActivity")

	time.sleep(60)

	flag = 1

	onactivityvalue = 0

	while flag != 4:
		result_onactivitymemoryvalue = os.popen("adb shell dumpsys meminfo com.xiaomi.loan")

		text_onactivitymemoryvalue = result_onactivitymemoryvalue.read()

		a = text_onactivitymemoryvalue.split()

		once_onactivityvalue = a.index("TOTAL")

		once_onactivityvaluenum = a[once_onactivityvalue + 1]

		onactivityvalue = onactivityvalue + int(once_onactivityvaluenum)

		result_onactivitymemoryvalue.close()

		time.sleep(30)

		flag = flag + 1

	onactivityvaluetransfer = round((onactivityvalue/(3*1024)),2)

	return onactivityvaluetransfer

def GetOnBackMemoryValue():
	os.popen("adb shell am start -W com.xiaomi.loan/com.xiaomi.jr.app.MiFinanceActivity")

	time.sleep(60)

	os.popen("adb shell input keyevent 3")

	time.sleep(30)

	os.popen("adb shell am send-trim-memory --user 0 com.xiaomi.loan  COMPLETE")

	time.sleep(180)

	flag = 1

	onbackvalue = 0

	while flag != 4:
		result_onbackmemoryvalue = os.popen("adb shell dumpsys meminfo com.xiaomi.loan")

		text_onbackmemoryvalue = result_onbackmemoryvalue.read()

		a = text_onbackmemoryvalue.split()

		once_onbackvalue = a.index("TOTAL")

		once_onbackvaluenum = a[once_onbackvalue + 1]

		onbackvalue = onbackvalue + int(once_onbackvaluenum)

		result_onbackmemoryvalue.close()

		time.sleep(30)

		flag = flag + 1

	onbackvaluetransfer = round((onbackvalue / (3 * 1024)), 2)

	return onbackvaluetransfer









