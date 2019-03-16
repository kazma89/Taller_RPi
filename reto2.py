import RPi.GPIO as GPIO #Importamos la libreria GPIO para controlar los pines del RPi
import time #Importamos la libreria time para darle pausas al programa

#Declarando pines
ledPin = 11
ledPin2 = 12
ledPin3 = 13

#Setup
GPIO.setmode(GPIO.BOARD) #Seteamos los pines para usarlos según el número en la placa
GPIO.setwarnings(False) #Quitamos las advertencias es el programa
GPIO.setup(ledPin, GPIO.OUT) #Seteamos el ledPin como salida
GPIO.setup(ledPin2, GPIO.OUT) #Seteamos el ledPin2 como salida
GPIO.setup(ledPin3, GPIO.OUT) #Seteamos el ledPin3 como salida

#Loop
try:
    while True:
        #Encendemos los LEDs en secuencia
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(ledPin2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(ledPin3, GPIO.HIGH)
        time.sleep(0.2)
        #Apagamos los LEDs en secuencia
        GPIO.output(ledPin3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(ledPin2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(ledPin3, GPIO.LOW)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()