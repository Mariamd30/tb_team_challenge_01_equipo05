![Cabecera](./assets/cabecera_git_codespaces.png)

# 🚀 GitHub Codespaces para el Bootcamp

## 1. ¿Qué es GitHub Codespaces?

GitHub Codespaces es un entorno de desarrollo en la nube basado en Visual Studio Code. Te permite escribir, ejecutar y debuggear código directamente en tu navegador sin necesidad de configuraciones locales complejas.

Es como tener un ordenador completo en el navegador: acceso a terminal, sistema de archivos, Python profesional con entornos virtuales, gestión de dependencias y variables de entorno de forma segura. Todo integrado con Git.

**Por qué lo usamos en el bootcamp:** Garantiza que todos trabajamos en el mismo entorno, sin problemas de "en mi máquina funciona".

---

## 2. Dónde encontrar Codespaces en GitHub Web

1. Ve a GitHub
2. En la esquina superior izquierda, haz click en el botón desblegable
3. Selecciona la pestaña **"Codespaces"**

![Botón Code en GitHub](<assets/Captura de pantalla 2026-05-19 a las 10.09.13.png>)

![Pestaña Codespaces abierta](<assets/Captura de pantalla 2026-05-19 a las 10.09.35.png>)

---

## 3. Cómo generar un Codespace

### Paso a paso:

1. GitHub → Repositorio → Botón "Code" → Pestaña "Codespaces"
2. Haz clic en **"Create codespace on main"** (o la rama que necesites)
3. Espera 1-2 minutos mientras se inicializa


![alt text](<assets/Captura de pantalla 2026-05-19 a las 10.10.35.png>)

![Interfaz de Codespaces](<assets/Captura de pantalla 2026-05-19 a las 10.11.35.png>)

## 4. Tres formas de trabajar en el Bootcamp

Tienes opciones según cómo quieras organizar tu trabajo.

### **Variante 1️⃣: Fork + Codespace en tu fork**

**Cuándo usarla:** Cuando quieres guardar tu trabajo versionado en tu cuenta de GitHub

**Pasos:**
1. Ve al repositorio oficial
2. Haz clic en **"Fork"** (arriba a la derecha) para copiar el repo a tu cuenta
3. Entra en tu fork
4. Botón "Code" → Codespaces → "Create codespace"
5. Trabajas, haces cambios y commit/push a tu fork

![Fork button en GitHub](<assets/Captura de pantalla 2026-05-19 a las 10.12.28.png>)
![alt text](<assets/Captura de pantalla 2026-05-19 a las 10.12.40.png>)

**Cómo guardar tus cambios (git add, commit, push):**

Una vez que hayas hecho cambios en tus archivos dentro de Codespaces:

1. Abre la **Terminal** en Codespaces (Ctrl+` o Terminal → New Terminal)
2. Guarda todos tus cambios:
   ```bash
   git add .
   ```
3. Crea un commit con un mensaje descriptivo:
   ```bash
   git commit -m "Descripción de los cambios que hiciste"
   ```
4. Sube los cambios a tu fork en GitHub:
   ```bash
   git push
   ```

Después de esto, tus cambios estarán en tu fork en GitHub. ¡Listo! Tu trabajo queda guardado y versionado.

---

### **Variante 2️⃣: Botón directo de la práctica (sin fork)**

**Cuándo usarla:** Cuando solo quieres experimentar y aprender sin complicaciones

**Cómo funciona:**
1. En algunas prácticas habrá un botón/enlace directo que dice algo como *"Abrir en Codespace"*
2. Haces clic
3. Se abre un Codespace automáticamente sin necesidad de fork
4. Trabajas en ese entorno
5. Puedes guardar tu trabajo localmente o descargarlo

![Botón de práctica que abre Codespace](<assets/Captura de pantalla 2026-05-19 a las 10.14.14.png>)
---

### **Variante 3️⃣: Fork + Clone local en VSCode**

**Pasos:**
1. Ve al repositorio oficial
2. Haz clic en **"Fork"**
3. En tu fork, botón "Code" → copia la URL HTTPS
4. En tu terminal local:
   ```bash
   git clone https://github.com/TU_USUARIO/REPOSITORIO_FORKEADO.git

   ```
5. Abre la carpeta en VSCode local
6. Trabaja, haz commit y push a tu fork

---

## 5. Personalizar tu Codespace: Cambiar el Tema

Codespaces usa VSCode, así que puedes cambiar el tema (tema claro/oscuro).

### Pasos:

1. Dentro de Codespaces, abre **Settings**:
   - En el engranaje (abajo a la izquierda) → "Settings"
   - O usa el atajo: `Cmd+,` (Mac) / `Ctrl+,` (Windows/Linux)

2. Selecciona **Temas** en el desplegable y luego, **Temas de color**

3. Selecciona el tema que prefieras:
   - **Light:** fondo blanco, texto oscuro
   - **Dark:** fondo oscuro, texto claro
   - Otros temas disponibles

4. Se aplica automáticamente

![Settings panel en Codespaces](<assets/Captura de pantalla 2026-05-19 a las 10.14.51.png>)

![Color Theme selector](<assets/Captura de pantalla 2026-05-19 a las 10.15.20.png>)