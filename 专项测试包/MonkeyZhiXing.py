#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮
import os
import time
import CreateTimeStamp

def Memory_Leak_Monkey():
	os.popen("adb shell monkey -v --throttle 300 --pct-touch 30 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 -p com.xiaomi.loan 10000>d:\MemoryLeak%d.txt" % CreateTimeStamp.gettimestamp())

def Jankey_Frame_Monkey():
	os.popen("adb shell monkey -v --throttle 300 --pct-touch 30 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 -p com.xiaomi.loan 1000>d:\JankeyFrame%d.txt" % CreateTimeStamp.gettimestamp())


