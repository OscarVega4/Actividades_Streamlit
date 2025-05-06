import streamlit as st
import pandas as pd

# ✅ Esta debe ser la primera llamada de Streamlit
st.set_page_config(
    page_title="Explorador de Música Electrónica",
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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

# Cargar datos
df = pd.read_csv("musica_electronica.csv")

st.title("🎧 Explorador de Música Electrónica")
st.markdown("Explora subgéneros, artistas y tracks usando `.loc` y `.iloc`")

# Mostrar el DataFrame completo
st.subheader("🎼 Base de datos completa")
st.dataframe(df)

# Sidebar - Filtros
st.sidebar.title("🔍 Filtros")

# Filtro por subgénero
subgeneros = st.sidebar.multiselect("Selecciona subgéneros", options=df["subgenero"].unique())
if subgeneros:
    df = df.loc[df["subgenero"].isin(subgeneros)]

# Filtro por país
paises = st.sidebar.multiselect("Selecciona países", options=df["pais"].unique())
if paises:
    df = df.loc[df["pais"].isin(paises)]

# Filtro por BPM
bpm_min, bpm_max = st.sidebar.slider("Rango de BPM", 90, 160, (110, 140))
df = df.loc[df["bpm"].between(bpm_min, bpm_max)]

# Filtro por disponibilidad
if st.sidebar.checkbox("Solo tracks disponibles"):
    df = df.loc[df["disponible"] == True]

# Mostrar DataFrame filtrado
st.subheader("🎚️ Resultados filtrados")
st.dataframe(df)

# Navegación por índice con iloc
st.subheader("🎯 Navegar por índice (usando `.iloc`)")
if len(df) > 0:
    index = st.number_input("Selecciona un índice de fila", min_value=0, max_value=len(df)-1, step=1)
    st.write(df.iloc[index])

# Edición de datos con loc
st.subheader("✏️ Editar BPM de un track (usando `.loc`)")

if not df.empty:
    indice_fila = st.selectbox("Selecciona el índice de la fila a editar", df.index.tolist())
    track_actual = df.loc[indice_fila]

    st.write("🎵 Track seleccionado:")
    st.write(track_actual)

    nuevo_bpm = st.number_input("Nuevo valor de BPM", min_value=60, max_value=200, value=int(track_actual["bpm"]))

    if st.button("Actualizar BPM"):
        df.loc[indice_fila, "bpm"] = nuevo_bpm
        st.success(f"BPM actualizado a {nuevo_bpm} para el track '{track_actual['track_name']}'")
        st.dataframe(df)