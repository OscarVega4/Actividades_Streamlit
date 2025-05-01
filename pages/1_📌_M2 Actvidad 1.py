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
    'Nombre': ['Ana', 'Juliana', 'Miguel', 'Alejandra'],
    'Edad': [23, 30, 27, 22],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Pereira']
}

df = pd.DataFrame(datos)

st.subheader("Tabla de personas")
st.dataframe(df)

st.subheader("Estadísticas")
st.write(df.describe(include='all'))

print(df)

libros = {
    "Título": ["Cien Años de Soledad", "1984", "Don Quijote de la Mancha", "El Principito"],
    "Autor": ["Gabriel García Márquez", "George Orwell", "Miguel de Cervantes", "Antoine de Saint-Exupéry"],
    "Año de Publicación": [1967, 1949, 1605, 1943],
    "Género": ["Realismo Mágico", "Distopía", "Novela de Caballería", "Fábula"]
}


df_libros = pd.DataFrame(libros)

st.subheader("Lista de libros")
st.dataframe(df_libros)

st.subheader("Estadísticas de los libros")
st.write(df_libros.describe(include='all'))
