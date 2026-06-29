![Cabecera](./assets/cabecera_vscode.png)
# Guía: VSCode para Trabajar con Ficheros

## 1. Introducción

Visual Studio Code (VSCode) es un **editor de código gratuito y ligero** desarrollado por Microsoft que usaremos durante todo el bootcamp para escribir y editar nuestros archivos de código.

¿Por qué VSCode?
- 📝 **Interfaz simple** pero poderosa
- 🚀 **Rápido y ligero** (no consume muchos recursos)
- 🔌 **Extensible** (puedes agregar funcionalidades)
- 🎨 **Personalizable** (temas, atajos, configuración)
- 🔗 **Integrado con Git** (muy útil para nuestro flujo de trabajo)

En esta guía aprenderás a usar VSCode como tu editor principal para el bootcamp.

### Vídeo de referencia

Si prefieres aprender viendo:
- [Primeros pasos en Visual Studio Code](https://drive.google.com/file/d/1FHOPEsELgUWmcqP-QPOD7jacVSfwiW_4/view?t=279.967514)

---

## 2. Instalación de VSCode

### Paso 1: Descargar VSCode

1. Ve a [code.visualstudio.com](https://code.visualstudio.com/)
2. Haz clic en el botón azul "Download"
3. Elige tu sistema operativo (Windows, Mac o Linux)

![CAPTURA: Página de descarga de VSCode](<./assets/Captura de pantalla 2026-05-12 a las 16.59.06.png>)

### Paso 2: Instalar

#### En Windows:
1. Ejecuta el instalador descargado
2. Acepta los términos de la licencia
3. En la sección "Select Additional Tasks", marca:
   - "Add to PATH" (importante para usar VSCode desde terminal)
   - "Add Open with Code action to Windows Explorer"
4. Haz clic en "Install"

#### En Mac:
1. Abre el archivo descargado
2. Arrastra VSCode a la carpeta "Applications"
3. Espera a que se copie

#### En Linux:
\`\`\`bash
# En Ubuntu/Debian
sudo apt-get install code

# O descarga el .deb desde la web y ejecuta:
sudo dpkg -i code_*.deb
\`\`\`

### Paso 3: Abrir VSCode por primera vez

Una vez instalado, abre VSCode. Verás la pantalla de bienvenida.

![**[CAPTURA: Pantalla de bienvenida de VSCode]**](<./assets/Captura de pantalla 2026-05-12 a las 16.58.44.png>)

---

## 3. Interfaz Principal de VSCode

Entender dónde está cada cosa te ayudará a moverte mejor.

### Las áreas principales

![**[CAPTURA: VSCode con áreas principales señaladas y etiquetadas]**](<./assets/Captura de pantalla 2026-05-12 a las 17.00.41.png>)

### 1. Barra de Actividades (izquierda, al lado del explorador)

Es la barra vertical con iconos. Desde aquí cambias entre vistas:

- **📁 Explorador** — Ver tus archivos y carpetas
- **🔍 Buscar** — Buscar en tus archivos
- **🌳 Control de Versiones** — Integración con Git
- **▶️ Ejecutar y Depurar** — Ejecutar tu código
- **📦 Extensiones** — Instalar add-ons

### 2. Explorador de Archivos

Aquí ves todos los archivos y carpetas de tu proyecto. Puedes:
- Hacer clic en un archivo para abrirlo
- Clic derecho para crear, copiar, eliminar
- Arrastrar archivos para organizarlos

### 3. Panel Principal (Editor)

El área grande en el centro donde escribes código. Puedes tener varios archivos abiertos en pestañas.

### 4. Terminal Integrada

Una terminal dentro de VSCode donde puedes ejecutar comandos (Git, comandos de terminal, etc.). Abrela con:
- \`Ctrl + ñ\` (Windows/Linux)
- \`Cmd + ñ\` (Mac)
- O Terminal → New Terminal en el menú

### 5. Barra de Estado

La línea inferior que muestra:
- Número de línea y columna donde está el cursor
- Tipo de archivo
- Encoding
- Rama de Git en la que estás

---

## 4. Leyenda de Iconos y Colores en los Archivos

En el Explorador y en las pestañas de archivos, verás diferentes iconos y colores que indican el estado de cada archivo. Aquí está el significado:

### Colores en el Explorador

| Color/Símbolo | Significa |
|---|---|
| ⚪ Blanco | Archivo guardado y sin cambios |
| 🟡 Amarillo/Naranja | Archivo modificado pero no guardado |
| 🔴 Rojo/Rosa | Archivo eliminado o no sincronizado con Git |
| 🟢 Verde | Archivo nuevo (nunca se ha guardado en Git) |

### En las Pestañas (tabs) del Editor

| Símbolo | Significa |
|---|---|
| **Punto blanco** • | El archivo tiene cambios sin guardar |
| **X** | Cerrar pestaña |
| **Sin punto** | El archivo está guardado |

### Iconos de Git en el Explorador

Si tu carpeta es un repositorio de Git, verás estos símbolos:

| Símbolo | Significa |
|---|---|
| **M** (Amarillo) | Modified — Archivo modificado |
| **U** (Rojo) | Untracked — Archivo nuevo no añadido a Git |
| **A** (Verde) | Added — Archivo preparado para commit (staged) |
| **D** (Rojo) | Deleted — Archivo eliminado |

### Barra de Estado (inferior)

En la parte inferior derecha de VSCode verás información:

\`\`\`
main | ⊙ (círculo) | cambios sin sincronizar
\`\`\`

Esto indica:
- **main** — la rama de Git en la que estás
- **⊙** — hay cambios sin sincronizar
- **cambios sin sincronizar** — número de archivos modificados

---

## 5. Abrir y Crear Archivos

### Abrir una carpeta existente

Así es como trabajarás la mayoría del tiempo:

1. Abre VSCode
2. Haz clic en File → Open Folder (o Ctrl+K Ctrl+O)
3. Selecciona la carpeta donde guardas tu código
4. Verás todos los archivos en el Explorador a la izquierda

![**[CAPTURA: VSCode con carpeta abierta mostrando estructura de archivos]**](<./assets/Captura de pantalla 2026-05-12 a las 17.02.00.png>)

### Crear un nuevo archivo

1. En el Explorador (izquierda), haz clic derecho en la carpeta
2. Selecciona "New File"
3. Escribe el nombre con extensión (ej: \`.ipynb\`, \`.py\`)
4. Presiona Enter

![**[CAPTURA: Menú contextual para crear archivo]**](<./assets/Captura de pantalla 2026-05-12 a las 17.02.22.png>)

### Crear una nueva carpeta

1. Clic derecho en el Explorador
2. "New Folder"
3. Dale un nombre

### Abrir un archivo rápidamente

Usa **Ctrl+P** (Cmd+P en Mac) para abrir la paleta rápida:

\`\`\`
Ctrl+P → empieza a escribir el nombre del archivo
\`\`\`

Es mucho más rápido que buscar en el Explorador.

![**[CAPTURA: Paleta rápida abierta mostrando búsqueda de archivo]**](<./assets/Captura de pantalla 2026-05-12 a las 17.02.46.png>)

---

## 6. Trabajar con Carpetas y Proyectos

### Estructura recomendada para el bootcamp

Te recomendamos organizar tu código con la misma estructura que usamos en el repositorio de clase.

### Navegar entre carpetas en VSCode

En el Explorador:
- Haz clic en la carpeta para expandirla (mostrar contenido)
- Haz clic en la flecha para contraerla (ocultarla)
- Doble clic en un archivo lo abre en el editor

![**[CAPTURA: Explorador mostrando estructura jerárquica de carpetas]**](<./assets/Captura de pantalla 2026-05-12 a las 17.02.00.png>)

### Cambiar de carpeta

Si necesitas abrir otro proyecto:
- File → Open Folder
- O arrastra otra carpeta al Explorador

### Guardar el espacio de trabajo

VSCode recuerda qué carpeta tenías abierta y qué archivos estaban abiertos. Cuando cierres y vuelvas a abrir, todo estará como lo dejaste.

---

## 7. Edición Básica: Atajos y Búsqueda

### Atajos de teclado principales

Estos atajos te ahorrarán mucho tiempo:

| Atajo | Qué hace |
|-------|----------|
| \`Ctrl+S\` (Cmd+S) | Guardar archivo actual |
| \`Ctrl+Shift+S\` | Guardar como (guardar con otro nombre) |
| \`Ctrl+Z\` | Deshacer |
| \`Ctrl+Y\` | Rehacer |
| \`Ctrl+X\` | Cortar línea |
| \`Ctrl+C\` | Copiar línea |
| \`Ctrl+V\` | Pegar |
| \`Ctrl+D\` | Seleccionar la palabra bajo el cursor |
| \`Ctrl+L\` | Seleccionar toda la línea |
| \`Alt+Arriba/Abajo\` | Mover línea hacia arriba/abajo |
| \`Ctrl+/\` | Comentar/descomentar línea |
| \`Ctrl+F\` | Buscar en el archivo |
| \`Ctrl+H\` | Buscar y reemplazar |

### Buscar en un archivo

1. Presiona **Ctrl+F**
2. Escribe lo que buscas
3. Presiona Enter o haz clic en los botones de navegación

Verá todos los resultados resaltados en el archivo.

### Buscar en toda la carpeta

1. Presiona **Ctrl+Shift+F**
2. Escribe el término a buscar
3. VSCode te mostrará todos los archivos que lo contienen

Muy útil cuando no recuerdas en qué archivo está algo.

### Reemplazar texto

1. Abre Buscar y Reemplazar: **Ctrl+H**
2. Escribe lo que buscas en el primer campo
3. Escribe el reemplazo en el segundo
4. Haz clic en "Replace" o "Replace All"

⚠️ **Cuidado**: "Replace All" reemplaza TODO de golpe. Verifica antes.

---

## 8. Extensiones Esenciales para el Bootcamp

Las extensiones son pequeños programas que añaden funcionalidades a VSCode. Estas son las que necesitarás para trabajar con Python, Jupyter y IA.

### Cómo instalar una extensión

1. Haz clic en el icono de Extensiones (izquierda) o presiona **Ctrl+Shift+X**
2. Busca el nombre de la extensión
3. Haz clic en "Install"
4. Espera a que se instale

![**[CAPTURA: Panel de extensiones abierto]**](<./assets/Captura de pantalla 2026-05-12 a las 17.03.25.png>)

### Extensiones recomendadas

| Nombre | Para qué sirve |
|--------|---|
| **Python** (Microsoft) | Soporte completo para Python — resaltado de sintaxis, debugging, linting |
| **Jupyter** (Microsoft) | Trabajar con notebooks \`.ipynb\` directamente en VSCode |
| **Data Wrangler** | Visualizar y manipular datos en pandas DataFrames |
| **Git Graph** | Visualizar rama de Git de forma gráfica |

### Instalar las 4 extensiones esenciales

Estas son **obligatorias** para tu bootcamp:

1. Abre el panel de extensiones (Ctrl+Shift+X)
2. Busca **"Python"** de Microsoft → Install
3. Busca **"Jupyter"** de Microsoft → Install
4. Busca **"Data Wrangler"** → Install
5. Busca **"Git Graph"** → Install

Una vez instaladas, VSCode reconocerá archivos \`.py\` y \`.ipynb\`, y podrás trabajar con notebooks sin problemas.

---

## 9. Trabajar con Ficheros en VSCode

En esta sección aprenderás a trabajar con dos tipos de archivos clave en el bootcamp: Jupyter Notebooks (.ipynb) para exploración de datos y Python scripts (.py) para crear programas ejecutables.

### 9.1 Trabajar con Jupyter Notebooks (.ipynb)

Los notebooks son archivos que mezclan código Python con explicaciones en Markdown. Son muy útiles para IA y ciencia de datos.

#### Qué es un Notebook (.ipynb)

Un notebook es como un cuaderno digital donde puedes:
- **Escribir código Python** en celdas
- **Ver resultados** inmediatamente debajo del código
- **Escribir explicaciones** en Markdown entre celdas
- **Incluir gráficos, tablas, imágenes** en los resultados

Es perfecto para explorar datos y aprender, porque ves el código y su resultado en el mismo lugar.

#### Qué es el Kernel

El **kernel** es el "motor" que ejecuta tu código Python. Es lo que realmente está corriendo tus instrucciones en la computadora.

Cuando abres un notebook:
1. VSCode carga el kernel de Python
2. Ese kernel espera a que ejecutes celdas
3. Cuando ejecutas una celda, el kernel la procesa
4. El kernel guarda la memoria (variables, funciones, datos) entre celdas

**Ejemplo**: Si en la celda 1 defines \`x = 5\`, el kernel lo recuerda, y en la celda 2 puedes usar \`print(x)\` sin volver a definirlo.

Si cierras y abres el notebook, el kernel se reinicia y pierde toda la memoria. Por eso verás "Restart kernel" en algunas ocasiones.

#### Abrir un notebook en VSCode

1. En VSCode, abre una carpeta que contenga un archivo \`.ipynb\`
2. Haz clic en el archivo \`.ipynb\` en el Explorador
3. Se abrirá dentro de VSCode mostrando las celdas

![**[CAPTURA: Notebook \`.ipynb\` abierto en VSCode]**](<./assets/Captura de pantalla 2026-05-12 a las 17.04.21.png>)

#### Ejecutar celdas en un notebook

- Haz clic en el botón "▶" (play) al lado de cada celda
- O presiona **Ctrl+Enter** para ejecutar la celda actual
- Los resultados aparecen debajo de la celda
- El kernel ejecuta el código y guarda las variables en memoria

#### Reiniciar el kernel

A veces el kernel se confunde o necesitas empezar de cero:
1. Haz clic en el icono "↻ Restart" en la parte superior del notebook
2. O presiona Ctrl+Shift+P → "Restart Kernel"

Esto borra toda la memoria del kernel. Las celdas no se ejecutan de nuevo, solo se limpia la memoria.

---

### 9.2 Ejecutar Archivos Python (.py) en Terminal

Una vez que hayas escrito código Python en un archivo \`.py\`, necesitarás ejecutarlo en la terminal para ver el resultado. VSCode tiene una terminal integrada que hace esto muy fácil.

#### Qué necesitas

- VSCode abierto con una carpeta de proyecto
- Un archivo \`.py\` creado (por ejemplo, \`ejemplo.py\`)
- Python instalado en tu computadora

#### Paso 1: Crear un archivo Python

Vamos a crear un ejemplo simple:

1. En el Explorador (izquierda), haz clic derecho en la carpeta
2. Selecciona "New File"
3. Escribe \`ejemplo.py\` y presiona Enter

#### Paso 2: Escribir código Python simple

Dentro del archivo \`ejemplo.py\`, escribe esto:

```python
print("hello world")
```

Este es el programa más simple de Python. Simplemente imprime el texto "hello world" en la pantalla.

Guarda el archivo con **Ctrl+S** (o Cmd+S en Mac).

![**[CAPTURA: archivo ejemplo.py con código]**](<./assets/Captura de pantalla 2026-05-13 a las 18.09.53.png>)

#### Paso 3: Abrir la Terminal Integrada

Ahora vamos a ejecutar el archivo. Abre la terminal integrada de VSCode:

- **Windows/Linux**: Presiona \`Ctrl+ñ\`
- **Mac**: Presiona \`Cmd+ñ\`
- O ve a **Terminal → New Terminal** en el menú

#### Paso 4: Ejecutar el archivo Python

En la terminal, escribe el comando para ejecutar Python:

```bash
python ejemplo.py
```

O, si tienes Python 3 específicamente:

```bash
python3 ejemplo.py
```

Presiona **Enter** para ejecutar.

#### Paso 5: Ver el resultado

Verás el resultado del programa en la terminal:

```
hello world
```
![**[CAPTURA: archivo ejemplo.py con código]**](<./assets/Captura de pantalla 2026-05-13 a las 18.10.15.png>)
---

## 10. Guardar y Sincronización

### Guardando archivos

**Guardar un archivo:**
\`\`\`
Ctrl+S (Windows/Linux)
Cmd+S (Mac)
\`\`\`

Verás un punto blanco en la pestaña del archivo cuando hay cambios sin guardar. Desaparece cuando guardas.

### Guardar todos los archivos

\`\`\`
Ctrl+Shift+Alt+S
\`\`\`

Útil cuando tienes varios archivos abiertos.

### Auto-save (guardar automáticamente)

Si quieres que VSCode guarde automáticamente:

1. File → Preferences → Settings (o Ctrl+,)
2. Busca "Auto Save"
3. Cambia el valor a "onFocusChange" (guarda cuando cambias de ventana/archivo) o "afterDelay" (guarda cada N segundos)

![**[CAPTURA: Configuración de Auto Save]**](<./assets/Captura de pantalla 2026-05-12 a las 17.05.42.png>)

### Sincronización con Git

VSCode está integrado con Git. En el Explorador de Control de Versiones (icono de árbol a la izquierda) puedes:
- Ver archivos modificados
- Hacer stage (git add)
- Hacer commit
- Push/Pull

Para esto, necesitas tener Git instalado y estar en una carpeta con un repositorio Git.

---

## 11. Errores Comunes

### Error: "El archivo no se ve en el Explorador"

**Problema**: Creaste un archivo pero no aparece en VSCode.

**Solución**:
- Presiona Ctrl+Shift+P (Cmd+Shift+P en Mac)
- Escribe "Reload Window"
- Presiona Enter

Esto actualiza la vista de VSCode.

### Error: "Archivo guardado pero los cambios no se ven"

**Problema**: Guardaste el archivo pero en el navegador sigue el código viejo.

**Solución**:
- En el navegador, presiona Ctrl+Shift+R (fuerza recargar, borra caché)
- O abre las herramientas de desarrollador (F12) y vacía el caché

### Error: "No puedo ejecutar Live Server"

**Problema**: El botón de Live Server no aparece o no funciona.

**Solución**:
- Verifica que hayas instalado la extensión "Live Server"
- Abre un archivo \`.html\` (Live Server solo funciona con HTML)
- Clic derecho en el archivo → "Open with Live Server"
- Si sigue sin funcionar, reinicia VSCode

### Error: "Mi archivo tiene errores pero parece correcto"

**Problema**: VSCode muestra líneas rojas de error.

**Solución**:
- Puede ser un falso positivo o una extensión que interfiere
- Presiona Ctrl+Shift+P → "Developer: Reload Window"
- O desactiva la extensión que causa el problema

### Error: "He borrado algo y no puedo recuperarlo"

**Problema**: Borraste código por accidente.

**Solución**:
- Presiona **Ctrl+Z** repetidamente para deshacer hasta recuperar lo que querías
- Si cierras el archivo sin guardar, VSCode te preguntará si quieres guardar cambios

---

## 12. Referencia Rápida

### Atajos principales

| Atajo | Qué hace |
|-------|----------|
| \`Ctrl+S\` | Guardar |
| \`Ctrl+Z\` | Deshacer |
| \`Ctrl+Y\` | Rehacer |
| \`Ctrl+F\` | Buscar |
| \`Ctrl+H\` | Buscar y reemplazar |
| \`Ctrl+P\` | Abrir archivo rápidamente |
| \`Ctrl+/\` | Comentar línea |
| \`Alt+Arriba\` | Mover línea hacia arriba |
| \`Alt+Abajo\` | Mover línea hacia abajo |
| \`Ctrl+ñ\` | Abrir/cerrar terminal |
| \`Ctrl+Shift+X\` | Abrir extensiones |
| \`Ctrl+Shift+P\` | Paleta de comandos |

### Menús principales

- **File** — Crear, abrir, guardar archivos
- **Edit** — Editar (deshacer, rehacer, buscar)
- **View** — Cambiar la vista (mostrar/ocultar paneles)
- **Terminal** — Abrir terminal
- **Help** — Ayuda y documentación

### Extensiones que DEBES INSTALAR

1. **Python** — Para trabajar con archivos \`.py\`
2. **Jupyter** — Para trabajar con notebooks \`.ipynb\`
3. **Data Wrangler** — Para manipular datos en pandas
4. **Git Graph** — Para visualizar tu repositorio de Git

---

## ¿Necesitas ayuda?

Si algo no funciona:

1. Mira esta guía nuevamente
2. Revisa la sección de "Errores Comunes"
3. Pregunta a los profesores o compañeros
4. Mira los vídeos de referencia al inicio

¡Ahora estás listo para escribir código en VSCode! 🚀
