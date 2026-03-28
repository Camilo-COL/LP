ventas=[12000,80000,15000,4000,22000,7000,18000]
n_ventas=[1,2,3,4,5,6,7]

contador = 0 

for n in range(len(ventas)):
    v_v=ventas[n]
    numero=n_ventas[n]

    if v_v <= 7000:
        tipo="baja"
    elif v_v <= 15000:
        tipo="media"
    else:
        tipo="alta"
        contador += 1

    print("venta numero: ", numero, "valor: ", v_v, "tipo: ", tipo)
print("Cantidad de ventas altas:", contador)

