matriz = []


filas = 2
columnas = 3

for i  in reversed(filas):
    matriz.append([])
    for j in range (columnas):
        valor = int(input("Fila{}, Columna {}: ".format(1+1,j+1)))
        matriz[i].append(valor)

print()
for fila in matriz:
    print("[", end =" ")
    for elemento in fila :
        print("{:8.2f}".format(elemento), end = " ")
    print ("]")


print()