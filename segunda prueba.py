# mi nombre: Gustavo Adolfo Valencia Caicedo
# grupo: 213022A-2201
# programa: ingenieria electronica
# codigo fuente: autoria propia

# MATRIZ CON LOS RECURSOS Y HORAS TRABAJADAS

grupo_de_trabajo = [
    ["gustavo", 8, 8, 8, 8, 8],
    ["lina", 9, 9, 8, 9, 9],
    ["adolfo", 7, 8, 7, 8, 7],
    ["edien", 10, 9, 10, 9, 10],
    ["oscar", 8, 8, 10, 9, 10]
]

# FUNCION PARA CALCULAR HORAS Y CLASIFICAR

def calcular_horas(recurso):

    nombre = recurso[0]

    horas = recurso[1:]

    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total, clasificacion


# RECORRER LA MATRIZ Y MOSTRAR RESULTADOS

for persona in grupo_de_trabajo:

    nombre, total, clasificacion = calcular_horas(persona)

    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("---------------------------")