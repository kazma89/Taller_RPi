for num in range(0,3,1): #hacer un conteo de 2 en 2 hasta 10
	a = [1,2,3,4,5,6,7,6,5,4,3,2,1] #Esto es un arreglo
	#Aqui tenemos un ciclo FOR con una sentencia IF dentro!
	for elemento in a:
		if elemento == max(a): #Mira por el número más alto en a
			print(elemento*'=')
			print('Secuencia numero {}' .format(num+1))
		print(elemento*'=')