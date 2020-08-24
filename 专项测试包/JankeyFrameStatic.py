#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import os
import time
def JankeyFrameInitialize():
	os.popen("adb shell am start -n com.xiaomi.loan/com.xiaomi.jr.app.MiFinanceActivity")
	# #adb shell
	#
	# logcat | grep -i ActivityManager
	#
	# 在log中“ActivityManager:Displayed”之后的部分就含有am 命令需要的package和launchactivity
	time.sleep(15)


def getJankeyFrameInitializestatus() :


	JFIresult = os.popen("adb shell dumpsys gfxinfo com.xiaomi.loan reset")

	JFIresultdata = JFIresult.read()

	JFIresultdatalist = JFIresultdata.split()

	JFIdatasituation = JFIresultdatalist.index("frames:") + 1

	JFIdata = int(JFIresultdatalist[JFIdatasituation])

	JFIresult.close()

	return  JFIdata

def getJankeyFrameData():
	JFDresult = os.popen("adb shell dumpsys gfxinfo com.xiaomi.loan")

	JFDresultdata = JFDresult.read()

	JFDresultdatalist = JFDresultdata.split()

	JFDdata_JankeyFrames = JFDresultdatalist[(JFDresultdatalist.index("frames:") + 1)]

	JFDdata_JankeyFramesPercent = JFDresultdatalist[(JFDresultdatalist.index("frames:") + 2)]

	JFDdata_rendered = JFDresultdatalist[(JFDresultdatalist.index("rendered:") + 1)]

	JFDdata = [JFDdata_rendered,JFDdata_JankeyFrames,JFDdata_JankeyFramesPercent,]

	JFDresult.close()

	return JFDdata









