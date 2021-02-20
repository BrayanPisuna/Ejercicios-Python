# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print "Ingrese dos numeros"
	x = int(raw_input())
	z = int(raw_input())
	while (x!=z) or (x%2==0) or (z%2==0):
		print "Error...   Ingrese dos numeros iguales"
		x = int(raw_input())
		z = int(raw_input())
	cont = 1
	x1 = [[float() for ind0 in range(z)] for ind1 in range(x)]
	for i in range(1,x+1):
		for j in range(1,z+1):
			x1[i-1][j-1] = cont
			cont = cont+1
	print " "
	print "La matriz original es:"
	for i in range(1,x+1):
		print " "
		for j in range(1,z+1):
			print x1[i-1][j-1]," ",
	print " "
	print " "
	print "Matriz Final"
	for i in range(x,0,-1):
		print " "
		for j in range(z,0,-1):
			print x1[i-1][j-1]," ",
	print " "
	print " "

