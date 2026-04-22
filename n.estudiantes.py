# registrar notas estudiantes, muestra notas de estudiantes
# debe pedir cuantos estudiantes mayor a 0/crear arreglo
# mostrar estuduante1=notas
# notas se validan por condicionales entre 0 y 5
# calcula promedio y aprueba si es mayor a o =3
# cuantos aprobaron y cuantos no

while True:
    estudiantes = int(input("Ingrese el numero de estudiantes: "))
    if estudiantes > 0:
        break
    else:
        print("El numero de estudiantes debe ser mayor a 0. Intente nuevamente.")

while True:
    cnotas = int(input("Cuantas notas por alumno: "))
    if cnotas > 0:
        break
    else:
        print("Digite un numero mayor a 0")

# Crear arreglo para almacenar estudiantes y sus notas
registro_estudiantes = []
aprobados = 0
desaprobados = 0

# Registrar notas de cada estudiante
for e in range(1, estudiantes + 1):
    print(" Estudiante",e)
    notas = []
    
    # Pedir notas validadas
    for i in range(1, cnotas + 1):
        while True:
            nota = float(input("Nota",i))
            if 0 <= nota <= 5:  # Validar entre 0 y 5
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    
    # Calcular promedio
    promedio = sum(notas) / len(notas)
    
    # Determinar si aprueba (>= 3)
    resultado = "Aprobó" if promedio >= 3 else "No aprobó"
    
    if promedio >= 3:
        aprobados += 1
    else:
        desaprobados += 1
    
    # Guardar en el registro
    registro_estudiantes.append({
        "estudiante": e,
        "notas": notas,
        "promedio": round(promedio, 2),
        "resultado": resultado})

for registro in registro_estudiantes:
    print("Estudiante",registro,'estudiante'":")
    print(" Notas:",registro,"notas")
    print("  Promedio:",registro,"promedio")
    print(registro,"resultado")

print("Total aprobados: ", aprobados)
print("Total desaprobados: ", desaprobados)