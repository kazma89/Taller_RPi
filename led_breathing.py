mport RPi.GPIO as GPIO #Importamos la libreria GPIO para utilizar los pines
import time #Importamos la libreria time para darle una pausa
import math #Importamos la libreria math para obtener las funciones matematicas que queremos

#Declarando pines
pwmPin = 18
ledPin = 23

#Declaramos la variable para darle un porcentaje de brillo al LED pwm
brillo = 0

#Setup
#Indicamos que queremos llamar a los pines por el nombre que les dio el fabricante
GPIO.setmode(GPIO.BCM) 
#Indicamos que los pines que tienen LEDs son de salida
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)

#Creamos el objeto llamado pwm y le adjuntamos la propiedad a pwmPin
#y le ponemos la frecuencia que le queremos dar
pwm = GPIO.PWM(pwmPin, 200) 

#Inicializamos los pines
GPIO.output(ledPin, GPIO.LOW)
pwm.start(brillo)

#Creamos una funcion para mapear los valores
def mapFun(x, inLo, inHi, outLo, outHi):	
	inRange = inHi - inLo #Indicamos el rango de numeros que esperamos recibir
	outRange = outHi - outLo #Indicamos el rango de numeros que esperamos sacar
	inScale = (x -inLo) / inRange #normalizamos el rango
	return outLo + (inScale * outRange) #retornamos el valor mapeado

x = 0

#Loop
try:
	while 1:
		step = 0.1			
		brillo = mapFun(math.sin(x),-1,1,0,100)
		x += step #Incrementamos x
		pwm.ChangeDutyCycle(brillo)
		time.sleep(0.05)

except KeyboardInterrupt:
	pwm.stop() #Paramos el parpadeo de pwmPin
	GPIO.cleanup() #Apagamos los GPIO