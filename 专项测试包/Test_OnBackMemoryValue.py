#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import MemoryValueFunction

import time

MemoryValueFunction.InitializeAppStatus()

time.sleep(70)

OnBackValue = MemoryValueFunction.GetOnBackMemoryValue()

print("后台测试完毕，前台内存值为%.2fMB"%OnBackValue)