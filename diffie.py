import math
import sys
import random

def miller(n):
	probable = False
	if n > 3 and n % 2 != 0: # n debe ser mayor que 11 y ser impar
		m = n - 1
		s_d = sd(m) # Hay que expresar n - 1 como una potencia de 2 multiplicado por un numero impar: (2 ^ s) * d
		s = s_d[0]
		d = s_d[1]
		for a in xrange(2, n):
			probable = False
			x = pow(a, d, n) # Si x = 1 o x = n - 1 pasar
			if s > 1 and (x != 1 or x != n - 1):
				for r in xrange(1, s): # de r = 1 hasta s - 1
					temporal = int(math.pow(2, r) * d) # temporal = (2 ^ r) * d
					x = pow(a, temporal, n) # x = (a ^ temporal) mod n
					# x = {a ^ [(2 ^ r) * d]} mod n
					if x == 1 or x == n - 1: # Si al menos uno es igual a esos, entonces es posible que sea primo, rompe el ciclo secundario
						probable = True
						break
			elif x == 1 or x == n - 1: # Si s es igual a 1 y x igual a esos valores entonces es primo, rompe el ciclo principal
				probable = True
				break
			if not probable: # Rompe el ciclo principal
				break
	if n == 1:
		probable = False
	elif n == 2 or n == 3:
		probable = True
	return probable
	
def sd(m):
	s = 1
	d = 0
	while True:
		d = int(m / math.pow(2, s))
		if d % 2 == 0: # Hay que evaluar si el numero que multiplica es par o impar
			s += 1
		else:
			break
	return (s, d)

# miller y sd - > se ocupan para verificar que un numero es primo

def divisores(factores):
	contadores = []
	auxiliar = factores[0]
	suma = 0
	for i in xrange(0, len(factores)):
		if factores[i] == auxiliar:
			suma += 1
		else:
			contadores.append((auxiliar, suma))
			auxiliar = factores[i]
			suma = 1
		if i == len(factores) - 1:
			contadores.append((auxiliar, suma))
	divisores = []
	if len(factores) > 1:
		divisores = [1]
		for i in xrange(0, len(contadores)):
			posicionultimo = len(divisores) - 1
			auxiliar = contadores[i]
			factor = auxiliar[0] # factor primo
			repeticiones = auxiliar[1] # potencias del factor primo de arriba
			for j in xrange(0, posicionultimo + 1):
				temporal = factor * divisores[j] # temporal es igual al factor por cada uno de los factores primos
				for k in xrange(1, repeticiones + 1):
					divisores.append(temporal)
					temporal = factor * temporal # temporal se multiplica con el factor, es decir, con las potencias del factor
	elif factores[0] == 1:
		divisores = [1]
	else:
		divisores = [1]
		divisores.append(factores[0])
	divisores.sort()
	return divisores
	
def factorizar(n):
	factores = []
	if n > 1:
		for i in xrange(2, n + 1):
			while n % i == 0:
				n = n / i
				factores.append(i)
			if n == 1:
				break
	elif n == 1:
		factores.append(n)
	return factores

# divisores y factorizar - > se ocupan para verificar que un numero es generador de otro

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

# generador y validargenerador - > se ocupan para encontrar todos los generadores de un numero

def comprobargrupo(generadores, p):
	for i in generadores:
		grupo = []
		for j in xrange(1, p):
			auxiliar = pow(i, j, p)
			grupo.append(auxiliar)
		grupo.sort()
		print 'Generador: ' + str(i)
		print grupo

# solo para visualizar mejor que es un generador de un grupo

def funciones(parametros):
	p = parametros[0]
	g = parametros[1]
	x = parametros[2]
	y = parametros[3]
	fx = pow(g, x, p)
	fy = pow(g, y, p)
	llave = pow(fx, y, p)
	key = pow(fy, x, p)
	funciones = (fx, fy)
	llaves = (llave, key)
	print
	print 'funciones: fx, fy'
	print funciones
	print
	print 'llaves'
	print llaves
	

def diffie(p):
	isprime = miller(p) # p es primo o no
	if isprime:
		print
		print 'generadores'
		generadores = generador(p)
		print generadores
		#comprobargrupo(generadores, p)
		posicion = random.randrange(0, len(generadores))
		g = generadores[posicion]
		x = random.randrange(1, p)
		y = 0
		while y == x or y == 0:
			y = random.randrange(1, p)
		parametros = (p, g, x, y)
		print
		print 'p, g, x, y'
		print parametros
		funciones(parametros)
	else:
		print str(p) + ' no es un numero primo'

if len(sys.argv) != 2:
	print 'El numero de argumentos es invalido'
else:
	isnumber = True
	ispositive = True
	limite = 11
	for i in xrange(1, len(sys.argv)): # Desde sys.argv[1] hasta sys.argv[len(sys.argv) - 1]
		if not sys.argv[i].isdigit(): # Si alguno de los argumentos no son numeros
			isnumber = False
			break
		elif not int(sys.argv[i]) > limite:
			ispositive = False # Si alguno de los argumentos que si son numeros no son mayores que el limite
			break
	if isnumber and ispositive:
		p = int(sys.argv[1])
		diffie(p)
	else:
		print 'Todos los argumentos deben ser numeros enteros mayores que '  + str(limite)
