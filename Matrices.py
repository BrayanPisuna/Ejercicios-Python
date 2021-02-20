filas = 1
columnas = int (input("Introdusca el numero de columnas: "))

matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = str(input ("fila {}, Columna{} : ".format(i+1, j+1)))
        matriz[i].append(valor)  
        
print()

for filas in matriz:
    print ("[", end=" ")
    for elemento in filas:
        print ("{}".format(elemento), end = " ")
    print ("]")

print()

