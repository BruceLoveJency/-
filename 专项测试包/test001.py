#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import os

result_autoboot = os.popen("adb shell pidof com.xiaomi.loan")
text_monkey = result_autoboot.read()
if len(text_monkey) == 0:
    print("没有开机自启动")
    result_autoboot.close()
else:
    print("有开机自启动")
    result_autoboot.close()

