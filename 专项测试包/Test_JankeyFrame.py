#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import os
import time
import JankeyFrameStatic
import JudgeMonkeyStatus
import MonkeyZhiXing

JankeyFrameStatic.JankeyFrameInitialize()

intializestauts = JankeyFrameStatic.getJankeyFrameInitializestatus()

while True:
	if intializestauts == 0:
		print("Jankey Frame初始化完成")
		break
	time.sleep(5)
	intializestauts = JankeyFrameStatic.getJankeyFrameInitializestatus()

MonkeyZhiXing.Jankey_Frame_Monkey()

time.sleep(10)

while JudgeMonkeyStatus.judgemonkeystatus():
 	time.sleep(10)

JankeyTestResult = JankeyFrameStatic.getJankeyFrameData()


for i in "()%":
	JankeyTestResult[2] = JankeyTestResult[2].replace(i,"")

if float(JankeyTestResult[2])<= 20.00:
	print("测试结果通过，核心场景掉帧率为百分之%s"%JankeyTestResult[2])
else:
	print("测试结果失败，核心场景掉帧率为百分之%s"%JankeyTestResult[2])

