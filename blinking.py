import RPi.GPIO as GPIO #Importamos la libreria GPIO para utilizar los pines
import time #Importamos la libreria time para darle una pausa

#Declarando pines
pwmPin = 18
ledPin = 23
buttonPin = 17

#Declaramos la variable para darle un porcentaje de brillo al LED pwm
brillo = 75

#Setup
#Indicamos que queremos llamar a los pines por el nombre que les dio el fabricante
GPIO.setmode(GPIO.BCM) 
#Indicamos que los pines que tienen LEDs son de salida
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
#Indicamos que el pin del boton es de entrada y que utilizara un pull_up resistance
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Creamos el objeto llamado pwm y le adjuntamos la propiedad a pwmPin
#y le ponemos la frecuencia que le queremos dar
pwm = GPIO.PWM(pwmPin, 200) 

#Inicializamos los pines
GPIO.output(ledPin, GPIO.LOW)
pwm.start(brillo)

#Loop
try:
	while 1:
		#Si el boton no esta presionado
		if GPIO.input(buttonPin):
			#mantenga apagado ledPin y encendido pwmPin
			GPIO.output(ledPin, GPIO.LOW)
			pwm.ChangeDutyCycle(brillo)
		#Si el boton esta presionado
		else:
			#parpadee ledPin y cambie el brillo a pwm
			GPIO.output(ledPin, GPIO.HIGH)
			pwm.ChangeDutyCycle(brillo)
			time.sleep(0.5)
			GPIO.output(ledPin, GPIO.LOW)
			pwm.ChangeDutyCycle(100-brillo)
			time.sleep(0.5)
except KeyboardInterrupt:
	pwm.stop() #Paramos el parpadeo de pwmPin
	GPIO.cleanup() #Apagamos los GPIO
