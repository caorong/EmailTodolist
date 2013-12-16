#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apscheduler.scheduler import Scheduler
import time

sched = Scheduler()
# sched.daemonic = False
sched.start()

# Define the function that is to be executed
def my_job(text,t2):
    print text
    print t2

# The job will be executed on November 6th, 2009
# exec_date = date(2009, 11, 6)

# Store the job in a variable in case we want to cancel it
# job = sched.add_date_job(my_job, exec_date, ['text'])
job = sched.add_date_job(my_job, '2013-12-16 17:16:14', ['text',str('22')])
print job
time.sleep(50)
# Start the scheduler  
# sched = Scheduler()
# sched.add_interval_job(job,minutes=30)  
# sched.start()
