def retornar_respuesta(a,b):
   
    if a < b:
        resultado=a + b 
        print("si a < b se suma: ")
        
    if a > b :
        resultado = a - b 
        print("si a > b se resta : ")
        
    if a == b:
        resultado=a*b 
        print("si a = b se multiplica: ")
        
    if a == b*2 and b != 0:
        resultado=a/b  
        print("si a es el doble de b  o b es diferente de 0, se divide : ")
       
    else:
        print("gracias")
        
    return  resultado ;

# bloque principal
valor1=int(input("Ingrese el primer valor de A:"))
valor2=int(input("Ingrese el segundo valor de B:"))
print(retornar_respuesta(valor1,valor2))
