#inventartio dinamico
inventario=[]
codigo1=1 
while True:
#registrar producto
    def op1():
        global codigo1
        nombre=str(input("nombre del producto: "))
        precio=int(input("valor del producto: "))
        producto_nuevo={"codigo":codigo1,"nombre":nombre,"precio":precio}
        inventario.append(producto_nuevo)
        print(producto_nuevo)
        codigo1+=1
        return(f"producto nuevo: {producto_nuevo}")

#actualizar producto
    def op2():
        buscar=int(input("ingrese el codigo del producto: "))
        for p in inventario:
            if p["codigo"]==buscar:
                print(f"producto encontrado: {p} ")
                act=str(input("que deseas actualizar "))
                if act=="nombre":
                    cambio_n=str(input("que nombre le deseas poner "))
                    p["nombre"]=cambio_n
                    print(f"cambio hecho: {p}")
                elif act=="precio":
                    cambio_p=int(input("Que valor quieres ponerle al producto?: "))
                    p["precio"]=cambio_p
                    print(f"cambio hecho: {p}")
                break
            elif p["codigo"]!=buscar:
                print("revisa q sea correcto")

#3. eliminar productos
    def op3():
        buscar=int(input("ingrese el codigo del producto: "))
        for n in inventario:
            if n["codigo"]==buscar:
                print(f"producto encontrado: {n} ")
                delet=str(input("deseas eliminarlo? "))
                if delet=="si":
                    inventario.remove(n)
                    print("producto eliminado con exito")
                    break
                try:
                    buscar != n
                    print("revisa si el codigo esta bien")
                    

    print("1. Registrar producto")
    print("2. Actualizar producto")
    print("3. Eliminar productos")
    print("4. Buscar Producto")
    print("5. Mostrar todos los productos")
    op=int(input("elija una opcion"))
    if op==1:
        op1()
    elif op==2:
        op2()
    elif op==3:
        op3()
    elif op==4:
        op4()
    elif op==5:
        op5()
    else:
        print("elige una opcion posible")
