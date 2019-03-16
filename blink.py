import RPi.GPIO as GPIO #Importamos la libreria GPIO para controlar los pines del RPi
import time #Importamos la libreria time para darle pausas al programa

#Declarando pines
ledPin = 11

#Setup
GPIO.setmode(GPIO.BOARD) #Seteamos los pines para usarlos según el número en la placa
GPIO.setwarnings(False) #Quitamos las advertencias es el programa
GPIO.setup(ledPin, GPIO.OUT) #Seteamos el ledPin como salida

#Loop
try:
    while True:
        #Encendemos el LED
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.2)
        #Apagamos el LED
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()