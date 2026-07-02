# --- Apartado 1: Ingesta de datos ---
#importamos pandas.
import pandas as pd
#hacemos lista con los ficheros para mas abajo poder cargar los datos con un bucle.
ficheros = ['data/movies.csv', 'data/ratings.csv', 'data/tags.csv', 'data/links.csv']

#cargamos los ficheros en un bucle por comprensión:
dfs = {i: pd.read_csv(i) for i in ficheros}

#shape:
for ruta, df in dfs.items():
    print(f"Shape de {ruta}: {df.shape}")
#columnas:
for ruta, df in dfs.items():
    print(f"Columnas de {ruta}: {df.columns.tolist()}")
#dtypes:
for ruta, df in dfs.items():
    print(f"\n Tipos de datos en {ruta}:")
    print(df.dtypes)
#head:
for ruta, df in dfs.items():
    print(f"\n Primeras dos filas de {ruta} ")
    print(df.head(2))
#conteo de nulos:
for ruta, df in dfs.items():
    print(f"\n Nulos en {ruta}")
    print(df.isnull().sum())
    
# --- Apartado 2: columna `year` ---
import numpy as np
#función year_from_title
def year_from_title(titulo):
    titulo = str(titulo).strip()
    final = titulo[-6:]
    if final.startswith('(') and final.endswith(')') and final[1:5].isdigit():
        return final[1:5]
    else:
        return np.nan  

df_movies = dfs['data/movies.csv']
#print(df_movies)
#creamos la columna year en esa tabla usando la columna title
df_movies['year'] = df_movies['title'].apply(year_from_title)
df_movies['year'] = pd.to_numeric(df_movies['year'], errors="coerce")

#editamos title:
def edit_title(fila):
    if pd.notnull(fila['year']):
        return fila['title'][:-6].strip()
    else:
        return fila['title']

df_movies['title'] = df_movies.apply(edit_title, axis=1)


#sin año reconocible
sin = df_movies[df_movies['year'].isnull()]

print(f"Películas sin año reconocible: {len(sin)}")
print("\n Pequeña muestra:")
print(sin['title'].head(5))

# --- Apartado 3: Merge / join  ---
#extraemos los dataframes
df_movies = dfs['data/movies.csv']
df_ratings = dfs['data/ratings.csv']
df_tags = dfs['data/tags.csv']
df_links = dfs['data/links.csv']

#tabla película–usuario–rating
df_pelicula_usuario_rating = pd.merge(
    df_ratings, df_movies[['movieId', 'title', 'genres']],on='movieId',how='left')

#tabla película–tags
#definimos los índices
df_movies_id = df_movies.set_index('movieId')
#Unimos con join.
df_pelicula_tags = df_tags.join(
    df_movies_id[['title']], 
    on='movieId', how='left')

#printeamos las diez primeras líneas más cabecera de las dos tablas:
print("ESQUEMA CONSTRUIDO")
print(f"\n1. Tabla Película-Usuario-Rating (MERGE):")
print(f"   - Shape: {df_pelicula_usuario_rating.shape}")
print(f"   - Columnas: {df_pelicula_usuario_rating.columns.tolist()}")
print(df_pelicula_usuario_rating.head(10))

print(f"\n2. Tabla Película-Tags (JOIN):")
print(f"   - Shape: {df_pelicula_tags.shape}")
print(f"   - Columnas: {df_pelicula_tags.columns.tolist()}")
print(df_pelicula_tags.head(10))

#Justificación:
#En la tabla de ratings, las filas de las películas se multiplican porque una sola película recibe miles de votos de usuarios distintos.
#En la tabla de tags, el título se repite cada vez que un usuario diferente le añade una etiqueta nueva.
#Se pierden las películas que nadie ha visto ni etiquetado, al hacer Left Join priorizamos la actividad de los usuarios, por lo que
# si una película no tiene interacciones, no nos sirve.
#Es aceptable porque conservamos el 100% de las opiniones y votos reales de la gente sin alterar los datos originales, 
# que es lo que realmente queremos.

# --- Apartado 4: Agregaciones ---
peliculas = df_pelicula_usuario_rating.groupby('title').agg(
    total_votos=('rating', 'count'),
    nota_media=('rating', 'mean')).reset_index()

#las 5 películas con más votos:
print(peliculas.sort_values(by='total_votos', ascending=False).head(5))

#comparaciones usando expresion regular para buscar ese patron específico:
df_pelicula_usuario_rating['year'] = df_pelicula_usuario_rating['title'].str.extract(r'\((\d{4})\)').astype(float)
df_pelicula_usuario_rating['decada'] = (df_pelicula_usuario_rating['year'] // 10) * 10

#Creamos una columna para separar en dos grandes segmentos
def segmentar_epoca(row):
    if row['decada'] < 2000:
        return 'Cine Clásico (Siglo XX)'
    else:
        return 'Cine Moderno (Siglo XXI)'

df_pelicula_usuario_rating['segmento_epoca'] = df_pelicula_usuario_rating.apply(segmentar_epoca, axis=1)

#tabla resumen usando groupby para comparar:
tabla_resumen_epocas = df_pelicula_usuario_rating.groupby('segmento_epoca').agg(
    total_valoraciones=('rating', 'count'),
    nota_promedio=('rating', 'mean'),
    nota_minima=('rating', 'min'),
    nota_maxima=('rating', 'max')).reset_index()

print("TABLA RESUMEN: CINE CLÁSICO FRENTE A MODERNO")

# --- Apartado 5: Preguntas sobre `movies` ---


#1. películas listadas en movies
print(f"1. Total de películas listadas: {len(df_movies)}")

#2. más antiguas (menor año)
a_minimo = df_movies['year'].min()
mas_antiguas = df_movies[df_movies['year'] == a_minimo][['title', 'year']]
print(f"\n2. Películas más antiguas (Año mínimo encontrado: {a_minimo}):")
print(mas_antiguas)

# 3.Dracula en el título (sin distinguir mayúsculas)
dracula_count = df_movies['title'].str.contains('dracula', case=False, na=False).sum()
print(f"\n3. Películas con 'Dracula' en el título: {dracula_count}")

# 4.Títulos más comunes
print("\n4. Títulos más comunes (repetidos):")
print(df_movies['title'].value_counts().head(5))

# 5.Películas con Exorcist ordenadas de antigua a moderna
exorcist_pelis = df_movies[df_movies['title'].str.contains('exorcist', case=False, na=False)]
exorcist_ordenadas = exorcist_pelis.sort_values(by='year')[['title', 'year']]
print("\n5. Películas con 'Exorcist' ordenadas por año:")
print(exorcist_ordenadas)

# 6.con año 1950:
peli_1950 = (df_movies['year'] == 1950).sum()
print(f"\n6. Películas del año 1950: {peli_1950}")

# 7.entre 1950 y 1959 inclusive:
pelis_50s = df_movies['year'].between(1950, 1959).sum()
print(f"7. Películas de la década de los 50 (1950-1959): {pelis_50s}")

# 8.año de la película exacta "Batman" y contraste con otras:
batman_exacto = df_movies[df_movies['title'] == 'Batman'][['title', 'year']]
todas_batman = df_movies[df_movies['title'].str.contains('batman', case=False, na=False)]
print("\n8. Película exacta 'Batman':")
print(batman_exacto)
print(f"   Contraste: Hay {len(todas_batman)} películas que contienen la palabra 'Batman'.")

# 9.películas que tienen como tag sci-fi y adventure:
tags_interes = df_pelicula_tags[df_pelicula_tags['tag'].str.lower().isin(['sci-fi', 'adventure'])]
pelis_ambos_tags = tags_interes.groupby('title').filter(lambda x: x['tag'].str.lower().nunique() == 2)
print("\n9. películas con tags 'sci-fi' y 'adventure' a la vez:")
print(pelis_ambos_tags['title'].unique()[:10]) 

# 10.La tag más repetida:
df_tags['tag_limpio'] = df_tags['tag'].str.strip().str.lower()
tag_mas_comun = df_tags['tag_limpio'].value_counts().idxmax()
total_repeticiones = df_tags['tag_limpio'].value_counts().max()
print(f"\n10. La tag más repetida es '{tag_mas_comun}' (aparece {total_repeticiones} veces).")

# PARTE 2 API CON TTMB .......................................................................................................

import pandas as pd
import requests
from IPython.display import display ## Para que sea mas visual
## PASO 2 CARGAMOS LOS CSV --> MOVIES Y LINKS
movies = pd.read_csv("data/movies.csv")
links = pd.read_csv("data/links.csv")

## PASO 3 VERIFICACION DE CONTENIDO (COLUNAS, FILAS) Y TAMBIEN SI NOS DEVUELVE UN NAN
## QUE FILAS TENEMOS?
display(movies.head())
display(links.head())

## VER ESTRUCTURA
movies.info()
links.info()

## PASO 4 UNIR LOS DATASETS (MOVIES.CSV Y LINKS.CSV)
df = movies.merge(links, on="movieId")
display(df.head())

## PASO 5 SELECCIONAR LAS 10 PRIMERAS PELICULAS
movies10 = df[df["tmdbId"].notnull()].head(10)
display(movies10[["movieId", "title", "tmdbId"]])

## PASO 6 INTRODUCIR LA API KEY
from config import API_KEY
import requests
from config import API_KEY

def fetch_movie_details(tmdb_id):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        overview = data.get("overview", "")
        homepage = data.get("homepage", "")
        return overview, homepage
    else:
        print(f"Error {response.status_code} en película {tmdb_id}")
        return "", ""
    
## PASO 8 APLICAMOS EL "OVERVIEW" Y "HOMEPAGE" A LAS 10 PELICULAS
movies10["overview"], movies10["homepage"] = zip(
    *movies10["tmdbId"].apply(fetch_movie_details)
)

## PASO 9 RESULTADO FINAL
display(movies10[["title", "tmdbId", "overview", "homepage"]].style.hide(axis="index"))



## PARTE 3 SINOPSIS CON API GEMINI..............................................................................................


import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Parte 3: overview → overview_es con Gemini  ---
# Requiere: `movies10` de la Parte 2. pip install google-genai

import getpass
from google import genai
import numpy as np
import pandas as pd


if "GEMINI_API_KEY" not in os.environ:
    os.environ["GEMINI_API_KEY"] = getpass("Introduce tu GEMINI_API_KEY: ")
    
# 1) Crea el cliente
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = 'gemini-2.5-flash'

np.movies10 = 'Hola'


def summarize_overview_es(overview, title=""):
    
    if not overview or not str(overview).strip():
        return ""
    
    prompt = (
        f"Resume en español, en un máximo de 2 frases, la siguiente sinopsis "
        f"de la película '{title}':\n\n{overview}"
    )
    
    response = client.models.generate_content(
            model=MODEL,
            contents= prompt,
        )
    
    return response.text.strip()
    

overview_es_list = []

for idx, row in movies10.iterrows():
    resumen = summarize_overview_es(row.get("overview", ""), row.get("title", ""))
    overview_es_list.append(resumen)

movies10["overview_es"] = overview_es_list

for idx, row in movies10.head(3).iterrows():
    print(f"Título: {row['title']}")
    print(f"Overview (EN): {row['overview'][:150]}...")
    print(f"Overview (ES): {row['overview_es']}")
    print("-" * 80)