import streamlit as st
import pandas as pd
import io

st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

@st.cache_data
def cargar_datos():
    return pd.read_csv("estudiantes_colombia.csv")

df = cargar_datos()

st.title("📊 Análisis de Estudiantes en Colombia")

st.markdown("Esta aplicación permite visualizar y filtrar los datos del archivo `estudiantes_colombia.csv`.")

st.subheader("🔍 Primeras 5 filas del dataset")
st.dataframe(df.head())

st.subheader("🔍 Últimas 5 filas del dataset")
st.dataframe(df.tail())

st.subheader("🧾 Información general del dataset")
info_df = pd.DataFrame({
    "Columna": df.columns,
    "Tipo de dato": df.dtypes.astype(str),
    "Valores no nulos": df.notnull().sum(),
    "Valores nulos": df.isnull().sum()
})

st.dataframe(info_df)

st.subheader("📈 Estadísticas descriptivas")
st.dataframe(df.describe())

st.subheader("🧮 Seleccionar columnas para visualizar")
columnas = st.multiselect("Selecciona las columnas que deseas ver:", df.columns.tolist(), default=["nombre", "edad", "promedio"])
st.dataframe(df[columnas])

st.subheader("🎯 Filtrar estudiantes por promedio mínimo")
promedio_min = st.slider("Selecciona el promedio mínimo:", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
df_filtrado = df[df["promedio"] >= promedio_min]
st.write(f"Mostrando {len(df_filtrado)} estudiantes con promedio mayor o igual a {promedio_min}")
st.dataframe(df_filtrado)