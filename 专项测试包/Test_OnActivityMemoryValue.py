#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮
import time

import MemoryValueFunction

MemoryValueFunction.InitializeAppStatus()

time.sleep(70)

OnActivityValue = MemoryValueFunction.GetOnActivityMemoryValue()

print("前台测试完毕，前台内存值为%.2fMB"%OnActivityValue)
