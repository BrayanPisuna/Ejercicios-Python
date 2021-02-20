filas = 1
n = int (input("Introdusca el numero: "))

matriz = []
ma = []
if n % 2 !=1 :
    print('El número', n, 'es par no continua con el procedimiento')
if  n >= 5:
    if  n<=100 and n % 2 !=1:
        print('El número', n, 'es par no continua con el procedimeinto')
    else:
        for i in range(0, int(n)):
            matriz.append(i*i)

        print("Vector: ", end="")
        for i in range(len(matriz)):
            print(str(matriz[i]) + " ", end="")
        print()
        
        print("Elemento de la mitad del vector es: " + str(matriz[int(n) // 2]))
else:
    print("no cumple con la condicion")
print()





