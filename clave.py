t = 0
vector = []
while True:
    if(int(t) >= 5 and int(t) % 2 == 1):
        break
    t=input("Ingrese el tamaño del vector: ")
    if(int(t) < 5 or int(t) % 2 == 0):
        print("tamaño debe ser mayor o igual que cinco y un numero impar")

print("tamaño del vector elegido es: " + t)

for i in range(1, int(t) + 1):
    vector.append(i*i)

print("Vector: ", end="")
for i in range(len(vector)):
    print(str(vector[i]) + " ", end="")
print()

print("Elemento de la mitad del vector es: " + str(vector[int(t) // 2]))