# 🏆 Team Challenge 01 - Equipo 05 🚀

¡Bienvenidos al repositorio del Equipo 05! Este es nuestro primer Team Challenge, enfocado en el análisis y limpieza de datos con Python y Pandas.

## 👥 Integrantes del Equipo
* David Saiz Aguilera - @DavidSaizA
* Sergio Fernández Marcos - @sergiofm96-code
* Javier Corchado Fernandez - @TermiJP
* María Muriel Delgado - @Mariamd30

## 🎯 Objetivo del Reto
Resolver el caso 

## 📂 Estructura del Proyecto

### 🪵 Gestión del Proyecto (Scrum Master & Ágil)
* **Daily Stand-ups Rápidas:** Sincronizaciones para identificar bloqueos técnicos.
* **Mitigación de Impedimentos:** Supervisión activa coordinando la correcta configuración del entorno local y del flujo de Git.

### ⚙️ Control de Versiones y Trabajo en Equipo
* **Gitflow del proyecto:** Trabajamos en paralelo utilizando una rama principal (`main`) para producción, una rama de desarrollo (`develop`) y ramas específicas por tarea (`feature/Parte_1_Data_analytics_Pandas`, `feature/Parte_2_Peticion_HTTP_API_TMDB_nueva`, `feature/Parte_3_Sinopsis_español_con_Gemini`, `feature/Parte_4_extensiones_con_Gemini`).
* **Integración:** Todo el código ha sido integrado mediante *Pull Requests* revisadas y mergeadas en equipo, resolviendo conflictos antes del merge final.
* **Seguridad:** Uso estricto de `.gitignore` para salvaguardar entornos locales (`.env`) sin subir jamás credenciales privadas al repositorio.

---

## 🛠️ Instalación y Configuración

1. **Clonar el repositorio:**

🚀 Fases del Desarrollo (Contenido del Notebook)
📊 Parte 1: Data Analytics (Pandas)
Carga y EDA: Análisis exploratorio inicial sobre los datasets locales (movies, ratings, tags y links). Diagnóstico de nulos, dimensiones y tipos.

Esquema Unificado: Unión de las tablas para crear una matriz enriquecida de película-usuario-rating utilizando .merge(), y un histórico de película-tags optimizado mediante .join().

Análisis por Segmentos: Extracción y limpieza del año de estreno mediante expresiones regulares (year) para agrupar y comparar el volumen y satisfacción de los usuarios por décadas cinematográficas.

Resolución de Cuestionario: Respuestas automatizadas a métricas clave del catálogo (conteo, títulos repetidos, filtros temáticos como "Dracula" o "Exorcist", y conteo de tags más repetidas).

🌐 Parte 2: Enriquecimiento de Datos con la API de TMDB
Mapeo y filtrado del catálogo de películas haciendo uso del identificador tmdbId.

Conexión segura e implementación de la función fetch_movie_details consumiendo el endpoint GET /3/movie/{id}.

Construcción del DataFrame final movies10 enriquecido con los campos externos overview (en inglés) y homepage.

🤖 Parte 3: Sinopsis en Español con Gemini
Autenticación con Google AI Studio y despliegue del cliente oficial google-genai.

Diseño de la función summarize_overview_es(overview, title) para procesar el argumento original en inglés y devolver una sinopsis en español de máximo 2 frases (restringiendo llamadas a la API si el contenido está vacío).

Inyección automatizada de la columna overview_es en el catálogo final.

🌟 Parte 4: Extensiones Opcionales (Gemini)
A) Catálogo Ampliado: Implementación de consultas estructuradas en formato JSON por película para extraer y mapear nuevas variables: pitch_es (texto de cartelera), edad_sugerida e identificación precisa de exactamente 3 temas clave en español.

B) Recomendador por Género: Algoritmo que filtra los éxitos del catálogo (nota media y volumen mínimo de votos) cruzado con Gemini para formular recomendaciones personalizadas y justificadas en español.
   
### MEMORIA DEL PROYECTO

## 📊 Fase de Data Analytics: Parte 1 (Pandas)

Esta sección comprende el bloque inicial del proyecto, centrado en la ingesta, limpieza, transformación y análisis exploratorio del conjunto de datos cinematográficos alojado en la ruta `Team_Challenges/TC_01_Sprint_03_04/data/`.

### 1. Ingesta y Diagnóstico Inicial de Datos
Se automatizó la carga de los cuatro ficheros principales (`movies.csv`, `ratings.csv`, `tags.csv` y `links.csv`) mediante un bucle de comprensión utilizando **Pandas**, optimizando el almacenamiento en un diccionario de DataFrames (`dfs`). 

Para asegurar la integridad del ecosistema de datos antes de operar sobre ellos, se realizó una auditoría técnica automatizada evaluando:
* **Dimensión (`shape`):** Control del volumen total de registros y variables por archivo.
* **Esquema de datos (`columns`, `dtypes`):** Verificación de nombres de columnas y tipos de datos (numéricos, objetos, flotantes) para prever conversiones necesarias.
* **Inspección visual (`head`):** Validación de consistencia estructural de las primeras filas.
* **Calidad del dato (`isnull().sum()`):** Conteo de valores nulos para cuantificar el impacto del dato ausente.

---

### 2. Ingeniería de Características: Extracción y Limpieza de la Columna `year`
Los títulos originales de la tabla de películas contenían el año de estreno incrustado en formato de texto entre paréntesis al final de la cadena (ej. *"Toy Story (1995)"*). Con el fin de posibilitar análisis cronológicos, se aplicó el siguiente pipeline de transformación:

1.  **Aislamiento:** Se diseñó una función personalizada (`year_from_title`) para extraer los últimos 6 caracteres, validando mediante lógica condicional que cumplieran con el patrón numérico `(YYYY)`. En caso de no cumplirlo, se asignó un valor nulo (`NaN`) mediante **NumPy**.
2.  **Conversión de Tipos:** Se transformó la nueva columna `year` a tipo numérico (`float`) forzando errores a `NaN` para garantizar la viabilidad de operaciones matemáticas futuras.
3.  **Limpieza del Texto Primario:** Se actualizó la columna `title` aplicando una función que remueve el bloque del año e intervalos de espacios vacíos en los registros procesados con éxito, aislando el nombre limpio de la película.
4.  **Control de Calidad:** Se aislaron las películas sin año reconocible, calculando su volumen e imprimiendo una muestra para auditar excepciones en la nomenclatura de origen.

---

### 3. Integración de Estructuras (Merge y Join) y Justificación Técnica
Se construyó un nuevo esquema relacional para unificar las entidades del modelo. Se generaron dos grandes estructuras tabulares:

* **Tabla Película–Usuario–Rating (`MERGE`):** Se realizó una fusión de tipo *Left Join* tomando como base la tabla `ratings` y cruzándola con `movies` a través de la clave común `movieId`.
* **Tabla Película–Tags (`JOIN`):** Se modificó el índice de la tabla de películas a `movieId` para realizar un acoplamiento directo de tipo *Left Join* sobre la tabla de etiquetas (`tags`).

#### **Justificación del Modelo y Comportamiento de los Datos:**
> * **Efecto Multiplicador:** En la tabla de ratings, los registros de películas se duplican de forma esperada debido a que una sola pieza cinematográfica recibe miles de valoraciones por parte de distintos usuarios (relación 1 a Muchos). De forma homóloga, en la tabla de tags, el título se replica secuencialmente cada vez que un usuario añade una etiqueta nueva.
> * **Tratamiento de Pérdida de Registros:** Al implementar la estrategia de *Left Join*, se asume conscientemente la exclusión de aquellas películas del catálogo general que no registran ninguna interacción (sin votos ni etiquetas). 
> * **Aceptabilidad de la Estrategia:** Este criterio es metodológicamente correcto ya que el core del análisis prioriza la actividad orgánica y las opiniones reales de la muestra poblacional. Preservar películas huérfanas de datos de interacción alteraría las métricas y resúmenes estadísticos del comportamiento del consumidor.

---

### 4. Agregación, Segmentación e Insights del Negocio
Para extraer valor analítico, se ejecutaron operaciones de agregación y análisis macro-temporal:

* **Métricas por Título:** Mediante agrupaciones (`groupby('title')`) y funciones agregadas (`count` y `mean`), se calculó el volumen total de votos y la nota promedio por película, permitiendo identificar de forma matemática el *Top 5* de películas con mayor tracción en la plataforma.
* **Análisis Intergeneracional (Cine Clásico vs. Moderno):** A través de expresiones regulares (`str.extract`), se segmentaron las valoraciones en décadas. Posteriormente, se definió una función de negocio para clasificar los datos en dos macro-segmentos: **Cine Clásico (Siglo XX)** para producciones previas al año 2000 y **Cine Moderno (Siglo XXI)** para las posteriores.
* **Matriz Resumen:** Se computó una tabla agregada final comparando ambos bloques en función de: *Total de valoraciones*, *Nota promedio*, *Nota mínima* y *Nota máxima*. Esto nos permitió evaluar de manera formal la evolución de los estándares de puntuación y el volumen de consumo de la comunidad a lo largo del tiempo.

## 📊 Fase de Data Analytics: Parte 1 (Pandas)

Esta sección comprende el bloque inicial del proyecto, centrado en la ingesta, limpieza, transformación y análisis exploratorio del conjunto de datos cinematográficos alojado en la ruta `Team_Challenges/TC_01_Sprint_03_04/data/`.

### 1. Ingesta y Diagnóstico Inicial de Datos
Se automatizó la carga de los cuatro ficheros principales (`movies.csv`, `ratings.csv`, `tags.csv` y `links.csv`) mediante un bucle de comprensión utilizando **Pandas**, optimizando el almacenamiento en un diccionario de DataFrames (`dfs`). 

Para asegurar la integridad del ecosistema de datos antes de operar sobre ellos, se realizó una auditoría técnica automatizada evaluando:
* **Dimensión (`shape`):** Control del volumen total de registros y variables por archivo.
* **Esquema de datos (`columns`, `dtypes`):** Verificación de nombres de columnas y tipos de datos (numéricos, objetos, flotantes) para prever conversiones necesarias.
* **Inspección visual (`head`):** Validación de consistencia estructural de las primeras filas.
* **Calidad del dato (`isnull().sum()`):** Conteo de valores nulos para cuantificar el impacto del dato ausente.

---

### 2. Ingeniería de Características: Extracción y Limpieza de la Columna `year`
Los títulos originales de la tabla de películas contenían el año de estreno incrustado en formato de texto entre paréntesis al final de la cadena (ej. *"Toy Story (1995)"*). Con el fin de posibilitar análisis cronológicos, se aplicó el siguiente pipeline de transformación:

1.  **Aislamiento:** Se diseñó una función personalizada (`year_from_title`) para extraer los últimos 6 caracteres, validando mediante lógica condicional que cumplieran con el patrón numérico `(YYYY)`. En caso de no cumplirlo, se asignó un valor nulo (`NaN`) mediante **NumPy**.
2.  **Conversión de Tipos:** Se transformó la nueva columna `year` a tipo numérico (`float`) forzando errores a `NaN` para garantizar la viabilidad de operaciones matemáticas futuras.
3.  **Limpieza del Texto Primario:** Se actualizó la columna `title` aplicando una función que remueve el bloque del año e intervalos de espacios vacíos en los registros procesados con éxito, aislando el nombre limpio de la película.
4.  **Control de Calidad:** Se aislaron las películas sin año reconocible, calculando su volumen e imprimiendo una muestra para auditar excepciones en la nomenclatura de origen.

---

### 3. Integración de Estructuras (Merge y Join) y Justificación Técnica
Se construyó un nuevo esquema relacional para unificar las entidades del modelo. Se generaron dos grandes estructuras tabulares:

* **Tabla Película–Usuario–Rating (`MERGE`):** Se realizó una fusión de tipo *Left Join* tomando como base la tabla `ratings` y cruzándola con `movies` a través de la clave común `movieId`.
* **Tabla Película–Tags (`JOIN`):** Se modificó el índice de la tabla de películas a `movieId` para realizar un acoplamiento directo de tipo *Left Join* sobre la tabla de etiquetas (`tags`).

#### **Justificación del Modelo y Comportamiento de los Datos:**
> * **Efecto Multiplicador:** En la tabla de ratings, los registros de películas se duplican de forma esperada debido a que una sola pieza cinematográfica recibe miles de valoraciones por parte de distintos usuarios (relación 1 a Muchos). De forma homóloga, en la tabla de tags, el título se replica secuencialmente cada vez que un usuario añade una etiqueta nueva.
> * **Tratamiento de Pérdida de Registros:** Al implementar la estrategia de *Left Join*, se asume conscientemente la exclusión de aquellas películas del catálogo general que no registran ninguna interacción (sin votos ni etiquetas). 
> * **Aceptabilidad de la Estrategia:** Este criterio es metodológicamente correcto ya que el core del análisis prioriza la actividad orgánica y las opiniones reales de la muestra poblacional. Preservar películas huérfanas de datos de interacción alteraría las métricas y resúmenes estadísticos del comportamiento del consumidor.

---

### 4. Agregación, Segmentación e Insights del Negocio
Para extraer valor analítico, se ejecutaron operaciones de agregación y análisis macro-temporal:

* **Métricas por Título:** Mediante agrupaciones (`groupby('title')`) y funciones agregadas (`count` y `mean`), se calculó el volumen total de votos y la nota promedio por película, permitiendo identificar de forma matemática el *Top 5* de películas con mayor tracción en la plataforma.
* **Análisis Intergeneracional (Cine Clásico vs. Moderno):** A través de expresiones regulares (`str.extract`), se segmentaron las valoraciones en décadas. Posteriormente, se definió una función de negocio para clasificar los datos en dos macro-segmentos: **Cine Clásico (Siglo XX)** para producciones previas al año 2000 y **Cine Moderno (Siglo XXI)** para las posteriores.
* **Matriz Resumen:** Se computó una tabla agregada final comparando ambos bloques en función de: *Total de valoraciones*, *Nota promedio*, *Nota mínima* y *Nota máxima*. Esto nos permitió evaluar de manera formal la evolución de los estándares de puntuación y el volumen de consumo de la comunidad a lo largo del tiempo.

# MEMORIA TÉCNICA — Ejercicio 2  
## Enriquecimiento de datos de películas mediante la API de TMDB

---

## 1. Introducción

En este ejercicio se trabaja con el dataset MovieLens, que contiene información básica sobre miles de películas. El objetivo principal es enriquecer estos datos locales utilizando información externa obtenida a través de la API de The Movie Database (TMDB).

Se usan dos archivos CSV:

- `movies.csv`: títulos y géneros.
- `links.csv`: identificadores externos (`imdbId`, `tmdbId`).

El identificador `tmdbId` permite acceder a la API de TMDB para obtener, entre otros campos:

- `overview` (sinopsis)
- `homepage` (página oficial)

---

## 2. Objetivos

- Realizar un análisis de los datos.
- Identificar la clave común para unir los datasets.
- Seleccionar un subconjunto de películas con `tmdbId` válido.
- Conectarse a la API de TMDB de forma segura.
- Obtener información externa y añadirla al DataFrame.
- Presentar los resultados de forma clara y estructurada.

---

## 3. Metodología

### 3.1 Carga de datos

Se cargan los archivos CSV con Pandas y se inspeccionan sus primeras filas y estructura (`head()`, `info()`) para comprender el contenido y tipos de datos.

### 3.2 Análisis de los CSV

Se revisan:

- Columnas disponibles en cada CSV.
- Tipos de datos.
- Presencia de valores nulos.

Se identifica que `movieId` está presente en ambos archivos y puede utilizarse como clave para unirlos.

### 3.3 Unión de datasets

Se realiza la unión mediante:

```python
df = movies.merge(links, on="movieId")
# MEMORIA TÉCNICA — Ejercicio 3 
## Sinopsis generado por la API de Gemini

---

## 1. Introducción

En este ejercicio se trabaja con la API de Gemini para generar una sinopsis de 2 frases en español cogiendo de referencia la informacion de la columna overview de el DataFrame movie10. Y esta sinopsis se la metemos en una columna nueva llamada overview_es.

Se utiliza unicamente la API = GEMINI_API_KEY:

---

## 2. Objetivos

- Conexion correcta de la APi de Gemini.
- Verififcar que el prompt le llega a la API y lo ejecuta .
- Guardar de forma secreta la api_key para que no sea visible.
- Crear la columna overview_es en el Dataframe.
- Rellenar la columna overview_es con las sinopsis creadas por Gemini.

---

## 3. Metodología

### 3.1 Creacion de la clave de api_key

Nos metemos a google ai studio y creamos una clave de api con el formato de pago gratuito y nos creamos un .env para meter la API y no sea accesible

### 3.2 Llamada a Gemini

- Creamos response y guardamos ahi la informacion de la API
- Guardamos el prompt ya que no es necesario cambiarlo
- Verificar que la api_key funciona correctamente


### Parte 4 Integración de Gemini mediante la API de Google 
1. Introducción 
En esta parte del proyecto se integró la API de Gemini con el objetivo de incorporar funcionalidades de inteligencia artificial. Para ello se configuró un cliente que permite conectar el proyecto con el modelo de Gemini y realizar consultas de forma sencilla y segura.
2. Objetivos 
Configurar la conexión con la API de Gemini. Gestionar la clave API de forma segura mediante un archivo .env. Crear un cliente reutilizable para realizar consultas al modelo. Comprobar que la integración funcionaba correctamente dentro del proyecto.
3. Metodología
3.1 Configuración 
Primero se instaló la librería necesaria para trabajar con la API de Gemini y se creó un archivo .env para guardar la clave API sin exponerla en el código.
3.2 Desarrollo 
Se implementó el archivo gemini_client.py, encargado de cargar la clave, establecer la conexión con la API e inicializar el modelo gemini-flash-latest. De esta forma, el resto del proyecto puede utilizar el cliente sin necesidad de repetir la configuración.
3.3 Comprobación 
Una vez implementada la conexión, se realizaron varias pruebas desde el notebook para comprobar que el modelo respondía correctamente y que la integración funcionaba como se esperaba.
4. Incidencias 
Durante el desarrollo aparecieron algunos conflictos al fusionar las ramas con Git, además de un problema con el notebook, que quedó dañado durante el proceso. Finalmente, ambos inconvenientes se resolvieron y los cambios pudieron integrarse correctamente en la rama develop.
5. Resultado 
Se consiguió integrar correctamente la API de Gemini en el proyecto, dejando una configuración segura y un cliente reutilizable para realizar consultas al modelo. Tras resolver las incidencias surgidas durante el desarrollo, la funcionalidad quedó integrada y lista para su uso.

