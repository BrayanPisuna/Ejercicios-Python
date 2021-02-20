c = int(-1)

n = int (input("INGRESE EL VALOR DE N : "))
vec = [None]*n*n
matriz = [None]*n


if n < 3:
    print("comando no valido")
else:

    print(" ")
    print("DE Atras hacia Adelante")
    print(" ")

    for i in range(0,n):
        matriz[i] = [None]*n
        
    for i in range (n - 1 , -1 , -1):
        for j in range(n - 1 , -1 , -1):
            matriz[j][i]= int(input ("fila {}, Columna{} : ".format(i+1, j+1)))

    for i in range (n - 1 , -1 , -1):
        for j in range(n - 1 , -1 , -1):
            c=c+1;
            vec[c] = matriz[i][j]
        
   
    print(" ")
    print("Matriz")
    print(" ")

    for n in matriz:
        print ("[", end=" ")
        for elemento in n:
            print ("{}".format(elemento), end = " ")
        print ("]")

    print()


    impares = [numero for numero in vec if numero % 2 == 1 ]
    print("Impares ")
    print(impares)
    