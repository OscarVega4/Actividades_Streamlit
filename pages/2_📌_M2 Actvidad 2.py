import streamlit as st

# Configuración de la página
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

st.title("Actividad 1 - Creación de DataFrames")
st.write("El objetivo de esta actividad es aprender a crear y visualizar DataFrames usando Python y la biblioteca pandas.")

st.subheader("Descripción de la actividad")

datos = {
    'Nombre': ['Ana', 'Juliana', 'Miguel', 'Alejandra'],
    'Edad': [23, 30, 27, 22],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Pereira']
}

df = pd.DataFrame(datos)

st.subheader("Tabla de personas")
st.dataframe(df)

st.subheader("Estadísticas de personas")
st.write(df.describe(include='all'))

print(df)


libros = {
    "Título": [
        "Crimen y Castigo",
        "Orgullo y Prejuicio",
        "Matar a un Ruiseñor",
        "La Odisea"
    ],
    "Autor": [
        "Fiódor Dostoyevski",
        "Jane Austen",
        "Harper Lee",
        "Homero"
    ],
    "Año de Publicación": [
        1866,
        1813,
        1960,
        -800
    ],
    "Género": [
        "Novela psicológica",
        "Romance",
        "Drama social",
        "Epopeya"
    ]
}

df_libros = pd.DataFrame(libros)

st.subheader("Lista de libros")
st.dataframe(df_libros)

st.subheader("Estadísticas de los libros")
st.write(df_libros.describe(include='all'))


ciudades = [
    {"nombre": "Tokio", "población": 13960000, "país": "Japón"},
    {"nombre": "París", "población": 2148000, "país": "Francia"},
    {"nombre": "Ciudad de México", "población": 9200000, "país": "México"},
    {"nombre": "Buenos Aires", "población": 7744000, "país": "Argnetina"},
]

df_ciudades = pd.DataFrame(ciudades)

st.subheader("Información de Ciudades")

st.dataframe(df_ciudades)

st.subheader("Estadísticas de las ciudades")
st.write(df_ciudades.describe(include='all'))


productos = [
    ["Laptop", 3500.00, 10],
    ["Mouse", 25.99, 50],
    ["Teclado", 45.00, 30],
    ["Monitor", 1200.00, 15],
]

df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])

st.subheader("Productos en Inventario")

st.dataframe(df_productos)
st.subheader("Estadísticas de los productos")
st.write(df_productos.describe(include='all'))  


nombres = pd.Series(["Ana", "Juan", "Carla", "Mateo"])
edades = pd.Series([28, 34, 25, 40])
ciudades = pd.Series(["Medellín", "Armenia", "Manizales", "Pereira"])

# Combinar las Series en un diccionario
datos = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}

df_personas = pd.DataFrame(datos)

st.subheader("Datos de Personas")

st.dataframe(df_personas)


df = pd.read_csv("data.csv")

st.subheader("Datos desde CSV")
st.dataframe(df)

st.subheader("Datos desde Excel")

try:
    df = pd.read_excel("data.xlsx", engine="openpyxl")

    st.dataframe(df)
except FileNotFoundError:
    st.error("El archivo 'data.xlsx' no se encuentra en el directorio del proyecto.")

    
st.subheader("Datos de Usuarios desde JSON")

df = pd.read_json("data.json")


st.subheader("Datos de Música")

archivo_csv = "genres_v2.csv"  

df = pd.read_csv(archivo_csv)

st.dataframe(df)

st.subheader("Datos desde SQLite")

conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    calificacion REAL NOT NULL
)
""")

cursor.execute("SELECT COUNT(*) FROM estudiantes")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO estudiantes (nombre, calificacion)
    VALUES (?, ?)
    """, [
        ("Ana Acevedo", 4.5),
        ("Miguel Arango", 3.9),
        ("Lucía Torres", 4.8)
    ])
    conn.commit()

df = pd.read_sql("SELECT * FROM estudiantes", conn)

st.dataframe(df)

conn.close()

st.subheader("Datos desde NumPy")

array = np.array([
    [103, 202, 302],
    [405, 506, 609],
    [706, 808, 902]
])

columnas = ["Columna A", "Columna B", "Columna C"]
df = pd.DataFrame(array, columns=columnas)

st.dataframe(df)

st.subheader("Datos desde MongoDB")

try:
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["miapp"]
    coleccion = db["usuarios"]

    if coleccion.count_documents({}) == 0:
        coleccion.insert_many([
            {"nombre": "Juan Pérez", "ciudad": "Medellín"},
            {"nombre": "Ana Gómez", "ciudad": "Bogotá"},
            {"nombre": "Luis Torres", "ciudad": "Cali"}
        ])

    datos = list(coleccion.find({}, {"_id": 0}))

    if datos:
        df = pd.DataFrame(datos)
        st.dataframe(df)
    else:
        st.write("No hay datos disponibles en la colección.")

except Exception as e:
    st.error(f"Error al conectar con MongoDB: {e}")

