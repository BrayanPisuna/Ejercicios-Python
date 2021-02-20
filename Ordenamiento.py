N= int(input("Ingrese N: "))
A=[]

for I in range (N):
  A.append(int(input("Ingrese un numero: ")))  

A.sort()

print ("Lista ordenada: ", A)

positivos = 0
negativos = 0
ceros = 0

for I in range (A):  
     
    if A > 0:
        positivos += 1
    elif A < 0:
        negativos += 1
    else:
        ceros += 1  
    
print (" La cantidad de numeros positivos son:", positivos)      
print (" La cantidad de numeros Negativos son:", negativos)
print (" La cantidad de numeros Ceros son:", ceros)