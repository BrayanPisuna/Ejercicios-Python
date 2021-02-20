

n = int (input("ingrese el tamaño del vector: "))

if n % 2 !=1:
    print('El número', n, 'es par no continua con el procedimiento')
if  n > 5:
    print('El número', n, 'es par no continua con el procedimiento')
if  n<=100 and n % 2 !=1:
    print('El número', n, 'es par no continua con el procedimiento')
else:
    for x in range(0,n):
        print(x*x, end=" ")
