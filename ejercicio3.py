clavePrincipal=0

while clavePrincipal<=111111:
    clavePrincipal=int(input("Ingrese Su clave de seis dígitos: "))

clavePrincipal=str(clavePrincipal)
N=list(clavePrincipal)

ln=len(N)
A=[0]*ln

for i in range(0,ln):
    A[i]=int(N[i])

print("Clave Principal:",A)

impares = [numero for numero in A if numero % 2 == 1 ]
print("Clave 1 Impares ", impares)

pares = [numero for numero in A if numero % 2 == 0 ]
print( "Clave 2 Pares ", pares)



