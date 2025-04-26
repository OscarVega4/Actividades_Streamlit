import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

st.title("Actividad 1 - Creación de DataFrames")
st.write("El objetivo de esta actividad es aprender a crear y visualizar DataFrames usando Python y la biblioteca pandas.")


datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 30, 27, 22],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla']
}

df = pd.DataFrame(datos)

st.subheader("Tabla de personas")
st.dataframe(df)

st.subheader("Estadísticas")
st.write(df.describe(include='all'))

print(df)