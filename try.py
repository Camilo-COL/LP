inventario=[]
codigo1=1
nombre="pepe1"
precio=200000
pepe=f"nombre: {nombre}, codigo: {codigo1}, precio: {precio}"
inventario.append(pepe)
print(inventario)

def op2():
    buscar=int(input("ingrese el codigo del producto: "))
    encontrado=False
    for p in inventario:
        if p==buscar:
            print(f"producto encontrado: {p} ")
            encontrado = True
    else:
        print("no encontrado")
op=int(input("asdnsd"))
if op==2:
    op2()

