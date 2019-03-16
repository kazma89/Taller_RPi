print('Este es mi primer script en Python') #Este es un comentario
string1 = 'Hola'
string2 = 'mundo'

#Los strings pueden ser concatenados con + y repetidos con *
print(string1 + ' ' + string2 + '!'*3)

division = 2/3
print('2 dividido entre 3 es {}' .format(division)) #Se puede hacer referencia a una variable utilizando {}
print('o con menos puntos decimales: {: f}' .format(division)) #Se puede especificar un tipo de dato

import math #Podemos importar librerias también, se recomienda que sea lo primero en aparecer
string3 = 'mas'
print('Se puede imprimir {0} de una variable, aqui esta Pi:{1}. Y esta seria la {2} variable!' .format(string3,math.pi,3))

print('\n') #Salto de línea
for num in range(0,10,2): #hacer un conteo de 2 en 2 hasta 10
	print(num)

print('\n') #Otro salto de línea

a = [1,2,3,4,5,6,7,6,5,4,3,2,1] #Esto es un arreglo
#Aqui tenemos un ciclo FOR con una sentencia IF dentro!
for elemento in a:
	if elemento == max(a): #Mira por el número más alto en a
		print(elemento*'=')
		print('Llegamos al mayor')
	print(elemento*'=')