from PIL import Image
import base64
import sched, time
from io import BytesIO
import json
print 'iniciando programa...'
from socketIO_client_nexus import SocketIO, LoggingNamespace
print 'importando socketIO - client'

#image = json.dumps({'picture' : data.encode('latin-1')})
def getImageSrc():
	image = Image.open("image.jpg")
	buffered = BytesIO()
	image.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue())
	return img_str

#import RPi.GPIO as GPIO
#print 'importando modulo GPIO para raspberry...'

# Indicando al GPIO de agarrar el pin fisico del raspberry
#GPIO.setmode(GPIO.BOARD)


# Variables para el primer servo (first)

# Indicando el pin del primer servo (first)
#firstPin=11
# Preparando el GPIO para el primer servo
#GPIO.setup(firstPin, GPIO.OUT)
# Indicando que el pin del primer servo PWM
#first=GPIO.PWM(firstPin,50)
# Indica el angulo (90) del servo
#first.start(7)





scheduler = sched.scheduler(time.time, time.sleep)

def new_timed_call(calls_per_second, callback, *args, **kw):
    period = 1.0 / calls_per_second
    def reload():
        callback(*args, **kw)
        scheduler.enter(period, 0, reload, ())
    scheduler.enter(period, 0, reload, ())

#### example code ####







def set_servo_angle(angle, servo):
	if(servo == 'first'):
		DC=1./18.*(angle)+2
		#first.ChangeDutyCycle(DC)
		print DC
		print angle
	if(servo == 'second'):
		print 'servo second no programado'
	if(servo == 'third'):
		print 'servo third no programado'

def one_servo_angle(data):
	angle = data.get('angle')
	servo = data.get('servo')
	set_servo_angle(angle, servo)


#socketIO = SocketIO('http://nodetestfabio.herokuapp.com', verify=False)
socketIO = SocketIO('http://localhost:3000', verify=False)



def p(c):
	img_str = getImageSrc()
	socketIO.emit('python', img_str)

new_timed_call(30, p, '30')  # print '9' nine times per second
scheduler.run()

socketIO.on('servo_angle', one_servo_angle)
socketIO.wait()