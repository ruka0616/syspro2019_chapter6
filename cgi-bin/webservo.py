
#!/usr/bin/env python


import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<input type="text" name="rad">')
print('<input type="submit" name="submit">')
print('</form>')



GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

form = cgi.FieldStorage()
value = form.getfirst('rad')
#value=0
def setservo(angle):
    angle=angle*0.01+1.44
    a=(angle/20)*100
    servo.ChangeDutyCycle(a)
    time.sleep(1.0)


setservo(int(value))

GPIO.cleanup()


