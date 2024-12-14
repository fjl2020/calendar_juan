import calendar
from datetime import datetime

def imprimir_calendario(fecha_inicio, fecha_fin):
    # Convertir las fechas de cadena a objeto datetime
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    # Iterar a través de los meses en el rango de fechas
    for año in range(fecha_inicio.year, fecha_fin.year + 1):
        for mes in range(1, 13):
            # Verificar si el mes está dentro del rango de fechas
            if (año == fecha_inicio.year and mes < fecha_inicio.month) or (año == fecha_fin.year and mes > fecha_fin.month):
                continue
            
            # Imprimir el calendario del mesdir
            print(calendar.month(año, mes))

# Solicitar al usuario las fechas
fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")

# Imprimir el calendario
imprimir_calendario(fecha_inicio, fecha_fin)