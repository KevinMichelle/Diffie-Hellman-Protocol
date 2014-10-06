import math
import sy
import random
from miller import miller
from generadores import generador
from verificadores import sonNumeros

# miller -> se ocupa para verificar que un numero es primo
# generador -> se ocupa para encontrar todos los generadores de un numero

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

def hackeo(p, g, fx, fy):
	(temporal, hacked_x, hacked_y, last_k) = 0, 0, 0, 0
	(ishacked_x, ishacked_y) = False, False
	print '\nempieza el hack'
	for k in xrange(1, p):
		temporal = pow(g, k, p)
		if p < 100:
			print k, temporal
		if temporal == fx:
			hacked_x = k
			ishacked_x = True
		if temporal == fy:
			hacked_y = k
			ishacked_y = True
		if ishacked_x and ishacked_y:
			last_k = k
			print '\nlast k'
			print last_k
			print '\nhack terminado\n'
			break
	print 'x y'
	print hacked_x, hacked_y
	print '\n'

def funciones(p, g, x, y):
	fx = pow(g, x, p)
	fy = pow(g, y, p)
	llave = pow(fx, y, p)
	key = pow(fy, x, p)
	print
	print 'fx, fy'
	print fx, fy
	print
	print 'llaves'
	print llave, key
	return (fx, fy, key)
	

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
		print
		print 'p, g, x, y'
		print p, g, x, y
		resultados = funciones(p, g, x, y)
		fx = resultados[0]
		fy = resultados[1]
		hackeo(p, g, fx, fy)
	else:
		print str(p) + ' no es un numero primo'

if len(sys.argv) != 2:
	print 'El numero de argumentos es invalido'
else:
	isnumber = True
	limite = 11
	areNumber = sonNumeros(sys.argv) # Verificar que son numeros desde sys.argv[1] hasta sys.argv[len(sys.argv) - 1]
	if areNumber:
		p = int(sys.argv[1])
		if p > 11:
			diffie(p)
		else:
			print 'El numero debe ser mayor que 11'
	else:
		print 'Todos los argumentos deben ser numeros enteros'
