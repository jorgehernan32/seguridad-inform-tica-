inicio_rango = int(input("Ingresa el rango inicial: ")
final_rango = int(input("Ingresa el rango final: "))
inicio_tabla = int(input("Ingresa el inicio de la tabla: "))
final_tabla = int(input("Ingresa el final de la tabla: "))

final_rango += 1
final_tabla += 1
for j in range(inicio_rango, final_rango):
    for i in range(inicio_tabla, final_tabla):
    
        print(i, "x", j, "=", i * j)
    print()
inicio_rango = int(input("Ingresa el rango inicial: "))
final_rango = int(input("Ingresa el rango final: "))
inicio_tabla = int(input("Ingresa el inicio de la tabla: "))
final_tabla = int(input("Ingresa el final de la tabla: "))

final_rango += 1
final_tabla += 1
for j in range(inicio_rango, final_rango):
    for i in range(inicio_tabla, final_tabla):
    
        print(i, "x", j, "=", i * j)
    print()