
if __name__ == '__main__':
	print("Ingrese dos numeros") 
	x = int(input("Primer numero: "))
	z = int(input("segundo numero: "))
	while (x!=z) or (x%2==0) or (z%2==0):
		print ("Error...   Ingrese dos numeros iguales")
		x = int(input("Primer numero: "))
		z = int(input("Primer numero:"))
	cont = 1
	x1 = [[float() for ind0 in range(z)] for ind1 in range(x)]
	for i in range(1,x+1):
		for j in range(1,z+1):
			if i==j:
				x1[i-1][j-1] = cont
				cont = cont+2
			else:
				x1[i-1][j-1] = 0
	i = 1
	j = x
	cont1 = 1
	while cont1<=x:
		if i!=j:
			x1[i-1][j-1] = cont
			cont = cont+2
		j = j-1
		i = i+1
		cont1 = cont1+1
	print (" ")
	print ("La matriz original es:")
	print (" ")
	for i in range(1,x+1):
		for j in range(1,z+1):
			print ( x1[ i-1] [ j-1 ], end="  ")
		print (" ")

print("Gracias")