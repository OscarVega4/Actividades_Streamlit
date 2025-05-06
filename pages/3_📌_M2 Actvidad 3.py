import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

# Cargar el archivo CSV
df_nuevo = pd.read_csv("personas_colombia.csv")
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

# Filtro 1: Filtro por rango de edad
st.sidebar.subheader("1. Filtro por rango de edad")
activar_edad = st.sidebar.checkbox("Filtrar por rango de edad")
if activar_edad:
    min_edad = st.sidebar.slider("Edad mínima", 15, 75, 25)
    max_edad = st.sidebar.slider("Edad máxima", 15, 75, 50)
    df_nuevo = df_nuevo[df_nuevo['edad'].between(min_edad, max_edad)]

# Filtro 2: Filtro por municipios específicos
st.sidebar.subheader("2. Filtro por municipios")
activar_municipios = st.sidebar.checkbox("Filtrar por municipios")
if activar_municipios:
    municipios_seleccionados = st.sidebar.multiselect(
        "Selecciona municipios", 
        ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 
         'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 
         'Yopal', 'Leticia', 'Puerto Inírida']
    )
    if municipios_seleccionados:
        df_nuevo = df_nuevo[df_nuevo['municipio'].isin(municipios_seleccionados)]

# Filtro 3: Filtro por ingreso mensual mínimo
st.sidebar.subheader("3. Filtro por ingreso mensual mínimo")
activar_ingreso = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo")
if activar_ingreso:
    ingreso_minimo = st.sidebar.slider("Ingreso mensual mínimo", 800000, 12000000, 2000000)
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'] > ingreso_minimo]

# Filtro 4: Filtro por ocupación
st.sidebar.subheader("4. Filtro por ocupación")
activar_ocupacion = st.sidebar.checkbox("Filtrar por ocupación")
if activar_ocupacion:
    ocupaciones_seleccionadas = st.sidebar.multiselect(
        "Selecciona ocupaciones", 
        ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 
         'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero']
    )
    if ocupaciones_seleccionadas:
        df_nuevo = df_nuevo[df_nuevo['ocupacion'].isin(ocupaciones_seleccionadas)]

# Filtro 5: Filtro por tipo de vivienda no propia
st.sidebar.subheader("5. Filtro por tipo de vivienda no propia")
activar_vivienda = st.sidebar.checkbox("Filtrar personas sin vivienda propia")
if activar_vivienda:
    df_nuevo = df_nuevo[~(df_nuevo['tipo_vivienda'] == 'Propia')]

# Filtro 6: Filtro por nombres que contienen una cadena
st.sidebar.subheader("6. Filtro por nombre")
activar_nombre = st.sidebar.checkbox("Filtrar por nombre")
if activar_nombre:
    texto = st.sidebar.text_input("Ingresa una subcadena en el nombre")
    if texto:
        df_nuevo = df_nuevo[df_nuevo['nombre_completo'].str.contains(texto, case=False, na=False)]

# Filtro 7: Filtro por año de nacimiento específico
st.sidebar.subheader("7. Filtro por año de nacimiento")
activar_ano_nacimiento = st.sidebar.checkbox("Filtrar por año de nacimiento")
if activar_ano_nacimiento:
    ano_seleccionado = st.sidebar.selectbox(
        "Selecciona el año de nacimiento", 
        list(range(1949, 2010))
    )
    df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].dt.year == ano_seleccionado]

# Filtro 8: Filtro por acceso a internet
st.sidebar.subheader("8. Filtro por acceso a internet")
activar_internet = st.sidebar.checkbox("Filtrar por acceso a internet")
if activar_internet:
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    if acceso == "Sí":
        df_nuevo = df_nuevo[df_nuevo['acceso_internet'] == True]
    else:
        df_nuevo = df_nuevo[df_nuevo['acceso_internet'] == False]

# Filtro 9: Filtro por ingresos nulos
st.sidebar.subheader("9. Filtro por ingresos nulos")
activar_ingresos_nulos = st.sidebar.checkbox("Filtrar por ingresos nulos")
if activar_ingresos_nulos:
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'].isnull()]

# Filtro 10: Filtro por rango de fechas de nacimiento
st.sidebar.subheader("10. Filtro por rango de fechas de nacimiento")
activar_fechas = st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento")
if activar_fechas:
    fecha_inicio = st.sidebar.date_input("Fecha de nacimiento mínima", pd.to_datetime("1949-01-01"))
    fecha_fin = st.sidebar.date_input("Fecha de nacimiento máxima", pd.to_datetime("2009-12-31"))
    df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].between(fecha_inicio, fecha_fin)]

# Mostrar el DataFrame filtrado
st.write("Datos filtrados", df_nuevo)

