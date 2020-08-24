#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import BootTimeFunction

BootTimeOutPutValue = BootTimeFunction.getBootTimeData()

if  BootTimeOutPutValue[1] == "True":
	print("启动时间通过，启动时间为%sms"%BootTimeOutPutValue[0])
else:
	print("启动时间未通过，启动时间为%sms"%BootTimeOutPutValue[0])

