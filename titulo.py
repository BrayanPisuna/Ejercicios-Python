if __name__ == '__main__':
	print("Ingrese dos numeros")
	x = int(input())
	z = int(input())
	while (x!=z) or (x%2==0) or (z%2==0):
		print("Error...   Ingrese dos numeros iguales")
		x = int(input())
		z = int(input())
	cont = 1
	x1 = [[float() for ind0 in range(z)] for ind1 in range(x)]
	for i in range(1,x+1):
		for j in range(1,z+1):
			x1[i-1][j-1] = cont
			cont = cont+1
	print(" ")
	print("La matriz original es:")
	for i in range(1,x+1):
		print(" ")
		for j in range(1,z+1):
			print(x1[i-1][j-1]," ", end="")
	print(" ")
	print(" ")
	print("Matriz Final")
	for i in range(x,0,-1):
		print(" ")
		for j in range(z,0,-1):
			print(x1[i-1][j-1]," ", end="")
	print(" ")
	print(" ")

