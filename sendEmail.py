#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class HtmlEmail(object):
	def __init__(self):
		# print "init"
		self.me = "root@xxx.com"
		self.psw = "123456"
		pass

	def send_to(self ,you, info):
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "todolist 发出提醒了！！！"
		msg['From'] = self.me
		msg['To'] = you

		# Create the body of the message (a plain-text and an HTML version).
		text = ""
		html = """\
		<html>
		  <head></head>
		  <body>
		    <p>Hi!<br>
		       How are you? fine thank you , and you ? <br>
		       """+ info +"""<br>
		       Here is the <a href="http://www.python.org">link</a> you wanted.
		    </p>
		  </body>
		</html>
		"""

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')

		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best and preferred.
		msg.attach(part1)
		msg.attach(part2)

		# Send the message via local SMTP server.
		s = smtplib.SMTP('smtp.126.com')
		# sendmail function takes 3 arguments: sender's address, recipient's address
		# and message to send - here it is sent as one string.
		s.login(self.me,self.psw)
		s.sendmail(self.me, you, msg.as_string())
		s.quit()


if __name__ == '__main__':
	""" 
	following is just for test
	"""
	# me == my email address
	# you == recipient's email address
	me = "xx@126.com"
	you = "xx@qq.com"

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "todolist 发出提醒了！！！"
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = "Hi!\nHow are you?\nHere is 中文裁缝师 测试 the link you wanted:\nhttp://www.python.org"
	html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi!<br>
	       How are you? 派森 啊 唉 唉额额我去了哦<br>
	       Here is the <a href="http://www.python.org">link</a> you wanted.
	    </p>
	  </body>
	</html>
	"""

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# Send the message via local SMTP server.
	s = smtplib.SMTP('smtp.xx.com')
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.login('xx@xx.com','xxx')
	s.sendmail(me, you, msg.as_string())
	s.quit()