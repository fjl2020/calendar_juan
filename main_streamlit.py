import streamlit as st
import calendar
from datetime import datetime

def imprimir_calendario(fecha_inicio, fecha_fin):
    # Convertir las fechas de cadena a objeto datetime
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    # Crear un string para almacenar los calendarios
    calendarios = []

    # Iterar a través de los meses en el rango de fechas
    for año in range(fecha_inicio.year, fecha_fin.year + 1):
        for mes in range(1, 13):
            # Verificar si el mes está dentro del rango de fechas
            if (año == fecha_inicio.year and mes < fecha_inicio.month) or (año == fecha_fin.year and mes > fecha_fin.month):
                continue
            
            # Crear el calendario del mes
            cal = calendar.monthcalendar(año, mes)
            month_name = calendar.month_name[mes]
            table = f"### {month_name} {año}\n"
            table += "| Mo | Tu | We | Th | Fr | Sa | Su |\n"
            table += "|----|----|----|----|----|----|----|\n"
            for week in cal:
                table += "| " + " | ".join(f"{day if day != 0 else ' '}" for day in week) + " |\n"

            calendarios.append(table)

    return calendarios

# Título de la aplicación
st.title("Calendario Mensual")

# Entradas de fecha
fecha_inicio = st.date_input("Ingrese la fecha de inicio:", value=datetime.today())
fecha_fin = st.date_input("Ingrese la fecha de fin:", value=datetime.today())

# Botón para generar el calendario
if st.button("Generar Calendarios"):
    # Convertir las fechas a formato string
    fecha_inicio_str = fecha_inicio.strftime("%Y-%m-%d")
    fecha_fin_str = fecha_fin.strftime("%Y-%m-%d")
    
    # Imprimir el calendario
    calendarios = imprimir_calendario(fecha_inicio_str, fecha_fin_str)

    # Mostrar los calendarios en dos columnas
    num_calendarios = len(calendarios)
    cols = st.columns(2)

    for i, calendario in enumerate(calendarios):
        cols[i % 2].markdown(calendario)
