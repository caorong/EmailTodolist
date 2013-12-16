#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template
import bottle
import urllib2,sys,re,os,json

from apscheduler.scheduler import Scheduler
import time
import sendEmail

sched = Scheduler()
# sched.daemonic = False
sched.start()

"""
test url
http://localhost:8000/user/381983545@qq.com/time/5/info/我靠，我竟然收到了
"""

def my_job(send_to,send_info):
    print "start job ,params: ",send_to,send_info
    sendEmail.HtmlEmail().send_to(send_to,"lalala,it's time todo "+str(send_info))

def send_email_with_delay(to,sec,info):
    global sched
    job = sched.add_date_job(my_job, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+int(sec))), [to,info])
    print job

@route('/user/<to>/time/<sec>/info/<info>')
def set_notify_time(to,sec,info=""):
    """
    send email to  and sec
    """
    send_email_with_delay(to,sec,info)
    print to,sec,info
    return "email will be send at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+int(sec)))+" info:"+info
    # return to + " - "+str(sec)


# @route('/book/<id>/page/<pageno>')
# def getBookSounds(id,pageno):
#     #print id , pageno
#     url = 'http://www.yytingting.com/yyting/bookclient/ClientGetBookResource.action?bookId='+id +'&pageNum='+pageno+'&pageSize=50&token='+getToken()
#     global headers
#     req = urllib2.Request(url ,headers = headers)
#     html = urllib2.urlopen(req).read()
#     #decodejson = json.loads(html)
#     return html

# run(host='192.168.5.100', port=8080)

run(host='0.0.0.0', port=8000)
# 0.0.0.0
# bottle.run(server='gunicorn')

# if __name__ == '__main__':
# 	print yz()[1]
    # print getToken()
    # print getPageJson()
    # print showIndex(getPageJson())

# 	while 1:
# 		# print random()
# 		print getToken()
# 		sleep(1)
# 	# print singleToken
