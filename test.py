#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
	import sendEmail
	# sendEmail.send_email("123")
	e = sendEmail.HtmlEmail()
	# send_to("222")
	# dir(e)
	# e.send_to('xxxx@qq.com',"test data : 啊啊对的谔谔")
	import time
	print time.time()
	print time.localtime(time.time())
	# '2013-12-16 14:19:10'
	sec = 50
	re = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+int(sec)))
	print re
