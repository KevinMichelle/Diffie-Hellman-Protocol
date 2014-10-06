from factorizar import factorizar, divisores

# divisores y factorizar -> se ocupan para verificar que un numero es generador de otro

def generador(p):
	generadores = []
	factores = factorizar(p - 1)
	divisor = divisores(factores)
	for i in xrange(2, p - 1):
		esgenerador = validargenerador(i, divisor, p)
		if esgenerador: # es generador i de p
			generadores.append(i)
	return generadores

def validargenerador(g, divisores, m): # g es generador, m es el modulo
	esgenerador =  True
	for i in xrange(1, len(divisores) - 1): # no hay que evaluar el primer y ultimo divisor
		auxiliar = pow(g, divisores[i], m)
		if auxiliar == 1: # si al menos una de las evaluaciones es igual a 1, no es generador
			esgenerador = False
			break
	return esgenerador
