# 1/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: 刘津玮

import os
import time


def judgeapplicationstatus():

    os.popen("adb reboot")

    time.sleep(60)

    os.popen("adb shell input swipe 540 1300 540 500 100")

    time.sleep(5)

    result_autoboot = os.popen("adb shell pidof com.xiaomi.loan")

    text_monkey = result_autoboot.read()

    if len(text_monkey) == 0:
        result_autoboot.close()
        return False
    else:
        result_autoboot.close()
        return True
