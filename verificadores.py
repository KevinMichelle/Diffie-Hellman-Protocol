def sonNumeros(arreglo):
	areNumber = True
	for i in xrange(1, len(arreglo)):
		if not arreglo[i].isdigit(): # Si alguno de los argumentos no son numeros
			areNumber = False
			break
	return areNumber
