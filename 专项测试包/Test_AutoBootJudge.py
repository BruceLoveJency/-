#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import AutoBootJudegeFunction

autobootresult = AutoBootJudegeFunction.judgeapplicationstatus()

if autobootresult == False:
	print("测试结果通过，没有开机自启动")
else:
	print("测试结果未通过，开机自启动")