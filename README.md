EmailTodolist
=============

a simple todolist notifyer by email, bottle and apscheduler

## how to run it 

### first config the smtp in sendEmail.py
function __init__'s me and psw (line 12,13) and SMTP server (line 48)

### run it 
python todoRobot.py

### final 
open browser
in chrome just type 
http://localhost:8000/user/xx@qq.com/time/5/info/我靠，我竟然收到了

user = destination email
time = delay xx second
info = email contant

### And..
all files except sendEmail.py and todoRobot.py are just for test...