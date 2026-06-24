![!\[Cabecera\](../../assets/cabecera_colab.png)](assets/cabecera_colab.png)
# Guía: Google Colab para el Bootcamp

## 1. Introducción

Google Colab es una plataforma **gratuita en la nube** de Google que te permite escribir y ejecutar código Python en tu navegador sin instalar nada en tu ordenador.

¿Por qué Colab en el bootcamp?

En el bootcamp usaremos Colab para trabajar con los **notebooks de los Workouts**, sin tener que configurar nada en local.

- ☁️ **En la nube** — No necesitas instalar nada, solo un navegador
- 📊 **Ideal para notebooks** — Los `.ipynb` (Jupyter) funcionan perfectamente
- 🔗 **Integrado con GitHub** — Acceso directo a tus repositorios
- 💾 **Conectado con Google Drive** — Guarda tus archivos automáticamente


---

## 2. ¿Qué es Google Colab? Y sus similitudes con VSCode

### Google Colab

Google Colab es un entorno Jupyter alojado en la nube. Piénsalo como un "VSCode online pero especializado en notebooks".

**Características:**
- Ejecuta código Python directamente en celdas
- Mezcla código con explicaciones en Markdown (como Jupyter)
- Acceso a recursos de Google (Drive, Gmail, etc.)
- Acceso a GPU y TPU para machine learning

Igual que cundo usamos un Jupyter Notebook en VSCode, pero en la nube.

### Diferencias clave

- **VSCode es local** → Colab es en la nube
- **VSCode es flexible** → Colab es especializado en notebooks
- **VSCode necesita configuración** → Colab funciona al instante
- **VSCode está siempre disponible** → Colab se desconecta por inactividad

---

## 3. Configuración Inicial (Primera Vez)

La configuración es muy simple. Solo necesitas hacer esto una vez.

### Paso 1: Acceder a Google Colab

1. Ve a [colab.research.google.com](https://colab.research.google.com/)
2. Inicia sesión con tu **cuenta de Google del campus**
   - Si no tienes, crea una o usa tu Gmail personal

![**\[CAPTURA: Página de inicio de Google Colab\]**](<assets/Captura de pantalla 2026-05-14 a las 13.11.21.png>)

### Paso 2: Conectar tu repositorio de GitHub

1. Colab te recibirá con una ventana con varias opciones
2. Haz clic en la pestaña **GitHub**
3. En el campo de búsqueda, pega la URL de tu repositorio de clase:
   ```
   https://github.com/aie-online-tb/Privado-AIE-Online
   ```
4. Marca la casilla **"Include private repos"** (Incluir repositorios privados)

![CAPTURA](<assets/Captura de pantalla 2026-05-14 a las 13.13.15.png>)

5. Se abrirá un **popup de autorización de GitHub**
6. En el popup, haz clic en **Autorizar** o **Allow**
7. Esto da permiso a Colab para acceder a tus repositorios privados

![**\[CAPTURA: Ventana de autorización de GitHub\]**](<assets/Captura de pantalla 2026-05-14 a las 13.13.23.png>)

### Paso 5: Seleccionar repositorio

1. Después de autorizar, el repositorio debería aparecer en la lista
2. ¡Listo! Ya tienes Colab configurado. No tienes que hacer nada más.

![**\[CAPTURA: Repositorio apareciendo en la lista de Colab\]**](<assets/Captura de pantalla 2026-05-14 a las 13.15.47.png>)

---

## 4. Uso Durante el Curso

Así es como usarás Colab en cada Workout.

### Acceso a los Workouts

1. Entra en el **recurso de Workout** de la unidad que corresponda
2. Se abrirá una pestaña con un "centro de trabajo" que contiene:
   - Píldoras (vídeos educativos)
   y/o:
   - Ejercicios


### Abrir en Colab

1. Cuando veas un **botón que dice "Open in Colab"**, haz clic en él
2. Se abrirá el notebook en una **nueva pestaña de Colab**
3. Ahora puedes escribir código y ejecutarlo directamente

![**\[CAPTURA: Botón "Open in Colab" en el centro de trabajo\]**](<assets/Captura de pantalla 2026-05-14 a las 13.17.13.png>)

### Trabajar en Colab

1. Lee las instrucciones en las celdas de Markdown
2. Escribe tu código en las celdas de código
3. Ejecuta una celda: haz clic en el botón ▶ o presiona **Ctrl+Enter**
4. Los resultados aparecen debajo de la celda
5. Cuando termines, tus cambios se guardan automáticamente en Google Drive

---

## 5. Alternativa: Trabajar en Local con VSCode

Si prefieres trabajar en tu ordenador en lugar de en la nube, puedes hacerlo localmente.

### Opción Local

1. Clona el repositorio de clase
2. Copia los notebooks (`.ipynb`) a tu repositorio personal
3. Abre los notebooks en **VSCode** (con la extensión Jupyter instalada)
4. Trabaja como lo harías en Colab, pero en tu ordenador

Para más detalles sobre cómo trabajar localmente, consulta la **[Guía de Git](./guia_uso_git.md)** y la **[Guía de VSCode](./guia_vscode.md)**.

---

## 6. Errores Comunes y Soluciones

### Error: "No puedo autorizar GitHub"

**Problema**: El popup de autorización no aparece o rechaza tu credencial.

**Solución**:
- Asegúrate de estar en la pestaña **GitHub** (no en Drive)
- Intenta usar tu **cuenta de GitHub personal** si tienes una
- Borra cookies del navegador e intenta de nuevo

### Error: "El repositorio no aparece en la lista"

**Problema**: Pegaste la URL pero el repositorio no aparece.

**Solución**:
- Verifica que marcaste **"Include private repos"**
- Espera a que cargue la lista (puede tardar unos segundos)
- Intenta copiar solo el nombre del repositorio (sin `https://github.com/`)

### Error: "Se desconectó sin guardar mi trabajo"

**Problema**: Trabajaste durante mucho tiempo y Colab se desconectó.

**Solución**:
- Guarda con frecuencia: **Ctrl+S** o File → Save
- Ten cuidado con sesiones largas (máximo 12 horas)
- Usa **VSCode local** si necesitas sesiones más largas

### Error: "Cuota excedida en GPU"

**Problema**: Google te dice que has excedido tu cuota de GPU.

**Solución**:
- Usa CPU en lugar de GPU (la mayoría de ejercicios no necesita GPU)
- Espera un tiempo y vuelve a intentar
- En el dropdown de Runtime, selecciona "T4 GPU" en lugar de "A100"

### Error: "Mi notebook abre pero aparece vacío"

**Problema**: Abriste el notebook pero no se ve el contenido.

**Solución**:
- Recarga la página (F5 o Cmd+R)
- Intenta abrir el archivo directamente desde tu Google Drive
- Si persiste, crea un nuevo notebook y copia el contenido

---

## ¿Necesitas ayuda?

Si algo no funciona:
1. Mira esta guía de nuevo
2. Revisa la sección "Errores Comunes"
3. Pregunta a los profesores o compañeros
4. Consulta la documentación oficial: [colab.research.google.com/notebooks/basic_features_overview.ipynb](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)

¡Ahora estás listo para usar Colab! 🚀