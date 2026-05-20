# Matriz con nombre del recurso y horas trabajadas de lunes a viernes
recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 7, 8, 7],
    ["Luis", 9, 10, 9, 9, 10],
    ["María", 6, 7, 8, 7, 6]
]

# Función para calcular total de horas y clasificación
def calcular_horas(recurso):
    nombre = recurso[0]
    horas = recurso[1:]

    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# Mostrar resultados
print("REPORTE DE HORAS SEMANALES\n")

for recurso in recursos:
    nombre, total, clasificacion = calcular_horas(recurso)

    print("Recurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("---------------------------")