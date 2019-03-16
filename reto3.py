import RPi.GPIO as GPIO #Importamos la libreria GPIO para utilizar los pines
import time #Importamos la libreria time para darle una pausa

#Declarando pines
rojoVehPin = 18
amarilloVehPin = 23
verdeVehPin = 24
buttonPin = 17
verdePeaPin = 22
rojoPeaPin = 27


#Setup
#Indicamos que queremos llamar a los pines por el nombre que les dio el fabricante
GPIO.setmode(GPIO.BCM) 
#Indicamos que los pines que tienen LEDs son de salida
GPIO.setup(rojoPeaPin, GPIO.OUT)
GPIO.setup(verdePeaPin, GPIO.OUT)
GPIO.setup(rojoVehPin, GPIO.OUT)
GPIO.setup(amarilloVehPin, GPIO.OUT)
GPIO.setup(verdeVehPin, GPIO.OUT)
#Indicamos que el pin del boton es de entrada y que utilizara un pull_up resistance
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Inicializamos los pines
GPIO.output(rojoPeaPin, GPIO.LOW)
GPIO.output(verdePeaPin, GPIO.LOW)
GPIO.output(rojoVehPin, GPIO.LOW)
GPIO.output(amarilloVehPin, GPIO.LOW)
GPIO.output(verdeVehPin, GPIO.LOW)

#Loop
try:
	while 1:
		#Si el boton no esta presionado
		if GPIO.input(buttonPin):
			#mantenga encendido el rojoPeaPin y el verdeVehPin
			GPIO.output(rojoPeaPin, GPIO.HIGH)
			GPIO.output(verdeVehPin, GPIO.HIGH)
			#Si el boton esta presionado
		else:
			#haga la secuencia de luces
			time.sleep(3)
			GPIO.output(verdeVehPin, GPIO.LOW)
			for seccuencia in range(0,2,1):
				GPIO.output(amarilloVehPin, GPIO.HIGH)
				time.sleep(0.3)
				GPIO.output(amarilloVehPin, GPIO.LOW)
				time.sleep(0.3)
			GPIO.output(rojoVehPin, GPIO.HIGH)
			GPIO.output(verdePeaPin, GPIO.HIGH)
			time.sleep(5)
except KeyboardInterrupt:
	pwm.stop() #Paramos el parpadeo de pwmPin
	GPIO.cleanup() #Apagamos los GPIO
