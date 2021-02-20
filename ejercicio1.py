monto = float (input("Digite el monto $: "));
tarjeta= int(input("Digite el numero de tarjeta : "));

if tarjeta == 1: 
    total= monto * 0.25
    print("El aumento de su tarjeta sera de 25% : $  " , total)
    limite= monto + total 
    print("El limite d ela tarjeta es: $ ", limite)
if tarjeta == 2:
    total= monto * 0.35
    print("El aumento de su tarjeta sera de 35%: $ " , total)
    limite= monto + total 
    print("El limite d ela tarjeta es: $ ", limite)
if tarjeta == 3 :
    total= monto * 0.40
    print("El aumento de su tarjeta sera de 40%: $" , total)
    limite= monto + total 
    print("El limite d ela tarjeta es: $ ", limite)
if tarjeta >=4 and tarjeta <=10:
    total= monto * 0.50
    print("El aumento de su tarjeta sera de 50%: $ ", total)
    limite= monto + total 
    print("El limite de la tarjeta es: $ ", limite)
else:
    print("Gracias por su visita")