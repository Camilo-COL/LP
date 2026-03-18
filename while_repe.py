n=int(input("Ingrese un numero: "))
while n > 1:
    n=n/2
    print(n)
if n<=0:
    print("digite un numero mayor a 1")
elif n<1:
    print("se cumple que el numero es menor a 1")    

## para ciclo repetitvo "sin fin"
while True:
    n = int(input("Ingrese un numero: "))
    while n > 1:
            n = n / 2
            print(n)
    
    if n <= 0:
            print("digite un numero mayor a 1")
    elif n < 1:
            print("se cumple que el numero es menor a 1")
    
    otra = input("¿Querés hacer otro cálculo? (si/no): ")
    if otra != "si":
            print("Hasta luego.")
            break