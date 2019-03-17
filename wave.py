import math
import time

numCycle = 5

def sin(x):
	return math.sin(x)

x = 0 
while 1: #x < numCycle:
	bar = int(20*sin(x))
	x += 0.2 # x = x+0.2, esto ajusta la cantidad de caracteres a imprimir por linea
	print((20+bar)*'=') #El resultado de bar tirara numeros negativos por lo que se le suma 20 para que el minimo sea 1
	time.sleep(0.05)