#1/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: 刘津玮

import datetime
import time

def gettimestamp():
	datetime_now = datetime.datetime.now()
# 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
	date_stamp = str(int(time.mktime(datetime_now.timetuple())))

# 3位，微秒
	data_microsecond = str("%06d" % datetime_now.microsecond)[0:3]

	date_stamp = date_stamp + data_microsecond

	return int(date_stamp)