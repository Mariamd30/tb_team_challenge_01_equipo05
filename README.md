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
   