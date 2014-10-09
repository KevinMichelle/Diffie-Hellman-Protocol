import math
import sys
import random
from miller import miller
from generadores import generador

# miller -> se ocupa para verificar que un numero es primo
# generador -> se ocupa para encontrar todos los generadores de un numero

class Persona:

	def __init__(self, p, g, name):
		self.name = name
		self.p = p
		self.g = g
		self.llave_privada = random.randrange(1, p)
		self.eval = 0
		self.llave_compartida = 0
		self.evaluarLlave()
		
	def evaluarLlave(self):
		self.eval = pow(self.g, self.llave_privada, self.p)
			
	def construirLlave(self, res_distinto):
		self.llave_compartida = pow(res_distinto, self.llave_privada, self.p)
		
	def verPersona(self):
		print self.name, self.llave_privada, self.eval, self.llave_compartida
		
class Hacker(Persona):
		
	def __init__(self, p, g, name):
		self.name = name
		self.p = p
		self.g = g
		self.llave_privada = 0
		self.eval = 0
		self.llave_compartida = 0
	
	def hackeo(self, fx, fy):
		print
		print 'empieza el hackeo'
		for k in xrange(1, p):
			temporal = pow(self.g, k, self.p)
			print k, temporal
			if temporal == fx:
				self.llave_privada = k
				self.evaluarLlave()
				self.construirLlave(fy)
				break
			elif temporal == fy:
				self.llave_privada = k
				self.evaluarLlave()
				self.construirLlave(fx)
				break
		print 'fin del hackeo'
		print
		self.evaluarLlave()
		
class Diffie:

	def __init__(self, p):
		self.p = p
		self.g = 0
		self.generadores()
		self.Alice = Persona(self.p, self.g, "Alice")
		self.Bob = Persona(self.p, self.g, "Bob")
		self.Alice.construirLlave(self.Bob.eval)
		self.Bob.construirLlave(self.Alice.eval)
		self.Alice.verPersona()
		self.Bob.verPersona()
		self.Mallory = Hacker(self.p, self.g, "Mallory")
		self.Mallory.hackeo(self.Alice.eval, self.Bob.eval)
		self.Mallory.verPersona()
		
	def generadores(self):
		self.generadores = generador(self.p)
		posicion = random.randrange(0, len(self.generadores))
		self.g = self.generadores[posicion]
		
	def comprobargrupo(generadores, p):
		for i in generadores:
			grupo = []
			for j in xrange(1, p):
				auxiliar = pow(i, j, p)
				grupo.append(auxiliar)
			grupo.sort()
			print 'Generador: ' + str(i)
			print grupo
			
	# solo para visualizar mejor que es un generador de un grupo, no utilizado
	

def main(p):
	isprime = miller(p) # p es primo o no
	if isprime:
		diffie = Diffie(p)
	else:
		print str(p) + ' no es un numero primo'

if len(sys.argv) != 2:
	print 'El numero de argumentos es invalido'
else:
	isnumber = True
	limite = 11
	if sys.argv[1].isdigit():
		p = int(sys.argv[1])
		if p > 11:
			main(p)
		else:
			print 'El numero debe ser mayor que 11'
	else:
		print 'Todos los argumentos deben ser numeros enteros'
