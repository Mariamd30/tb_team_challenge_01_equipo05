![Cabecera](./assets/cabecera_git.png)
# Guía: GitHub y tu Repositorio de Clase

## 1. Conceptos Fundamentales

Antes de empezar, es importante que entiendas qué es Git y GitHub, porque los usarás durante todo el bootcamp y tu carrera como desarrollador.

### ¿Qué es Git?

Git es un **software de control de versiones**. En palabras simples: es una herramienta que registra todos los cambios que haces en tus archivos de código, permitiendo que:

- 📝 **Guarde un historial** de todo lo que modificaste (quién cambió qué y cuándo)
- ⏮️ **Vuelvas atrás en el tiempo** si cometiste un error
- 🌳 **Trabajes en paralelo** con otras ramas de desarrollo sin afectar el código principal
- 👥 **Colabores en equipo** sin pisar el trabajo de otros

Cuando modificas un archivo y haces un "commit" (guardas), Git almacena exactamente qué líneas cambiaron. Es como tener un sistema de respaldos inteligente.


### ¿Qué es GitHub?

GitHub es un servicio en la nube (en internet) donde puedes **alojar tus repositorios** (carpetas controladas por Git). Durante el bootcamp usaremos GitHub de dos formas:

- **Repositorio de clase**: donde el profesor comparte las lecciones y material. Tú solo consultas, no modificas.
- **Tu repositorio personal**: donde trabajas con los ejercicios y guardas tu progreso.

Piénsalo así:
- **Git** = el sistema que controla tus cambios (funciona en tu ordenador)
- **GitHub** = el servidor donde guardas tus repositorios para que estén accesibles desde cualquier lugar

Con GitHub puedes:
- 💾 Guardar tu código en la nube (no pierdes trabajo si se daña tu ordenador)
- 📤 Compartir código con otros desarrolladores
- 👁️ Que otros vean tu trabajo y aprendan de ti
- 🔒 Tener repositorios privados (solo tú ves el código)
- 📚 Mantener siempre acceso al material más actualizado sin riesgo de perder tus cambios

### La Terminal

La **terminal** (o consola) es una ventana donde das órdenes a tu ordenador escribiendo comandos de texto.

En lugar de hacer clic en botones, escribes instrucciones. Por ejemplo:
```bash
git clone https://github.com/...
```

Cuando abres la terminal en VSCode, ves algo como:
```
usuario@ordenador ~/bootcamp %
```

Ese símbolo final (`%` o `$`) significa que la terminal está lista para que escribas un comando.

---

## 2. Configuración Inicial

### Paso 1: Crear cuenta de GitHub

1. Ve a [github.com](https://github.com)
2. Haz clic en "Sign up"
3. Rellena con tu correo, contraseña y usuario
4. Verifica tu email

### Paso 2: Instalar Git

Git es el programa que usa GitHub. Necesitas tenerlo instalado en tu máquina.

#### En Windows:
1. Ve a [git-scm.com](https://git-scm.com/download/win)
2. Descarga el instalador
3. Ejecuta el instalador y acepta las opciones por defecto

#### En Mac:
Abre Terminal y ejecuta:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
```

#### En Linux:
```bash
sudo apt-get update
sudo apt-get install git
```

### Paso 3: Configurar Git (importante)

Abre la terminal en VSCode y ejecuta estos comandos (copia tal cual, pero reemplaza los datos):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@example.com"
```

Verifica que funciona:
```bash
git config --list
```

![CAPTURA: Terminal de VSCode mostrando los comandos git config ejecutados y el resultado de git config --list](<./assets/Captura de pantalla 2026-05-12 a las 13.04.51.png>)
![CAPTURA: Terminal de VSCode mostrando los comandos git config ejecutados y el resultado de git config --list 2](<./assets/Captura de pantalla 2026-05-12 a las 13.06.16.png>)


### Paso 4: Generar clave SSH (opcional pero recomendado)

Esto hace que GitHub te reconozca sin pedir contraseña cada vez.

En la terminal de VSCode:
```bash
ssh-keygen -t ed25519 -C "tu.email@example.com"
```

Presiona Enter cuando pida ruta y contraseña (déjalas vacías).

Copia tu clave pública:
```bash
cat ~/.ssh/id_ed25519.pub
```

Luego en GitHub (arriba a la derecha, Settings → SSH and GPG keys → New SSH key) y pega tu clave.

![**[CAPTURA: Terminal mostrando el output del comando ssh-keygen]**](<./assets/Captura de pantalla 2026-05-12 a las 13.11.03.png>)

---

## 3. Clonar el Repositorio de Clase

### Paso 1: Encontrar el repositorio

Este será el repositorio:
```
https://github.com/aie-online-tb/Privado-AIE-Online
```

### Paso 2: Preparar la carpeta en tu ordenador

Decide dónde quieres guardar tus cosas. Por ejemplo:
- **Windows**: `C:\Users\TuUsuario\bootcamp`
- **Mac/Linux**: `~/bootcamp`

Abre VSCode, ve a Archivo → Abrir carpeta, y selecciona o crea esa carpeta.

![**[CAPTURA: VSCode mostrando la carpeta vacía abierta]**](<./assets/Captura de pantalla 2026-05-12 a las 13.09.38.png>)

### Paso 3: Clonar desde la terminal

Haz clic en Terminal → New Terminal (o Ctrl+`)

En la terminal, copia y ejecuta:
```bash
git clone https://github.com/nombre-organizacion/nombre-repo
```

Espera a que termine. Verás algo como:
```
Cloning into 'nombre-repo'...
remote: Enumerating objects: 234, done.
...
```

![**[CAPTURA: Terminal mostrando el proceso de clonación completo]**](<./assets/Captura de pantalla 2026-05-12 a las 13.09.52.png>)

### Paso 4: Explorar lo que clonaste

Abre la carpeta que se creó en VSCode:
```bash
cd nombre-repo
ls -la
```

Verás la estructura del curso.

![**[CAPTURA: Explorer de VSCode mostrando la estructura de carpetas clonada]**](<./assets/Captura de pantalla 2026-05-12 a las 13.11.28.png>)

---

## 4. Actualizar el Repositorio de Clase

Cada semana el profesor sube contenido nuevo. Para tener los cambios en tu ordenador:

### Comando para actualizar:

Desde la carpeta del repositorio:
```bash
git pull
```

Git te dirá qué cambios descargó.

### Cuándo ejecutarlo:

- Antes de cada clase
- Si el profesor te dice que hay contenido nuevo

```bash
# Ejemplo de output
cd nombre-repo
git pull
remote: Counting objects: 45, done.
Unpacking objects: 100% (45/45), done.
```

![**[CAPTURA: Terminal mostrando git pull y su output]**](<./assets/Captura de pantalla 2026-05-12 a las 13.12.15.png>)

---

## 5. Crear Tu Repositorio Personal

Este será tu espacio de trabajo. Aquí copiarás los archivos del repo de clase y harás tus ejercicios.

### Paso 1: Crear el repositorio en GitHub

1. En GitHub, haz clic en el "+" arriba a la derecha → New repository
2. Ponle un nombre descriptivo (ej: `bootcamp-mi-nombre`)
3. Selecciona **"Público"** MUY IMPORTANTE
4. Marca "Add a README file"
5. Haz clic en "Create repository"

![**[CAPTURA: Página de creación de nuevo repositorio en GitHub]**](<./assets/Captura de pantalla 2026-05-12 a las 13.13.05.png>)
![**[CAPTURA: Repositorio nuevo creado, mostrando el botón verde "Code"]**](<./assets/Captura de pantalla 2026-05-12 a las 13.13.39.png>)

### Paso 2: Clonar tu repositorio

Ve a tu repositorio, haz clic en el botón verde "Code" y copia la URL SSH (o HTTPS si no configuraste SSH).

En terminal:
```bash
cd ~/bootcamp  # o tu carpeta equivalente
git clone https://github.com/tu-usuario/bootcamp-mi-nombre
cd bootcamp-mi-nombre
```
### Paso 3: Copiar contenido del repo de clase

Cuando el profesor suba material nuevo al repositorio de clase, lo copias a tu repo personal.

```bash
cp -r ~/bootcamp/nombre-repo/* ~/bootcamp/bootcamp-mi-nombre/
```

![**[CAPTURA: Terminal mostrando el comando cp y su ejecución]**](<./assets/Captura de pantalla 2026-05-12 a las 13.14.35.png>)
![**[CAPTURA: VSCode mostrando los archivos copiados en tu repositorio]**](<./assets/Captura de pantalla 2026-05-12 a las 13.15.33.png>)

### Paso 4: Guardar los cambios (tu primer commit)

En tu repositorio personal:

```bash
cd ~/bootcamp/bootcamp-mi-nombre
git add .
git commit -m "Contenido inicial del curso"
git push
```

Esto sube tus cambios a GitHub.

![**[CAPTURA: Terminal mostrando add, commit y push completos]**](<./assets/Captura de pantalla 2026-05-12 a las 13.17.02.png>)
![CAPTURA: GitHub mostrando los archivos subidos en la web](<./assets/Captura de pantalla 2026-05-12 a las 13.17.18.png>)
---

## 6. Flujo Semanal

Aquí está el proceso que repetirás cada semana:

### 1. Actualizar el repo de clase (lunes o antes de clase)

```bash
cd ~/bootcamp/nombre-repo
git pull
```

### 2. Copiar nuevos archivos a tu repo

```bash
cp -r ~/bootcamp/nombre-repo/* ~/bootcamp/bootcamp-mi-nombre/
```

### 3. Trabajar en tu repo (durante la semana)

Haz los ejercicios en tu repositorio personal. Cuando termines un ejercicio o una sesión de trabajo:

```bash
cd ~/bootcamp/bootcamp-mi-nombre
git add .
git commit -m "Descripción de qué hiciste"
git push
```

**[CAPTURA: GitHub mostrando el historial de commits en tu repositorio]**

---

## 7. Errores Comunes y Soluciones

### Error: "git: command not found"

**Problema**: Git no está instalado o no se reconoce.

**Solución**: 
- Verifica que Git esté instalado: `git --version`
- Si no funciona, instálalo nuevamente (ver Paso 2 de Configuración Inicial)
- Reinicia VSCode después de instalar

### Error: "Permission denied (publickey)"

**Problema**: Git no puede conectar con GitHub. Usualmente es un problema de SSH.

**Solución**:
- Verifica que tu SSH key esté agregada a GitHub (Settings → SSH and GPG keys)
- Si no tiene SSH configurado, usa HTTPS en lugar de SSH
- O regenera la SSH key (ver Paso 4 de Configuración Inicial)

### Error: "fatal: Already exists and is not an empty directory"

**Problema**: Intentas clonar en una carpeta que ya existe.

**Solución**:
```bash
# Opción 1: Clona en una subcarpeta distinta
git clone https://github.com/... nombre-diferente

# Opción 2: Borra la carpeta existente (cuidado con esto)
rm -rf carpeta-existente
git clone https://github.com/...
```

### Error: Los archivos no aparecen después de clonar

**Problema**: Los archivos se descargaron pero no se ven en VSCode.

**Solución**:
- Presiona Ctrl+Shift+P (Cmd+Shift+P en Mac)
- Escribe "reload window" y presiona Enter
- También prueba: abre/cierra la carpeta en VSCode

### Error: Cambios que no se guardan con git push

**Problema**: Hiciste cambios pero GitHub no los muestra.

**Solución**: Asegúrate de hacer los tres pasos EN ORDEN:
```bash
git add .           # Agrega los cambios
git commit -m "..." # Confirma los cambios
git push            # Sube a GitHub
```

Si solo haces `add` y `commit`, los cambios no suben a GitHub.

---

## 8. Referencia Rápida de Comandos

Aquí está el resumen de todos los comandos que necesitas en tu día a día:

### Comandos Git Principales

| Comando | Qué hace |
|---------|----------|
| `git clone <url>` | Descargar un repositorio a tu ordenador |
| `git pull` | Actualizar tu copia con los cambios más recientes |
| `git status` | Ver qué archivos han cambiado |
| `git add .` | Preparar todos los cambios para guardar |
| `git commit -m "mensaje"` | Guardar los cambios con un mensaje descriptivo |
| `git push` | Subir tus cambios a GitHub |
| `git log` | Ver el historial de cambios |
| `git config --global user.name <nombre>` | Establecer tu nombre de usuario |
| `git config --global user.email <email>` | Establecer tu email |
| `git config --list` | Ver tu configuración actual |

### Comandos de Terminal

La terminal tiene sus propios comandos básicos para moverte por carpetas:

| Comando | Qué hace |
|---------|----------|
| `ls` | Listar archivos en la carpeta actual |
| `ls -a` | Listar archivos incluyendo los ocultos |
| `cd carpeta` | Entrar en una carpeta |
| `cd ..` | Salir de la carpeta (ir hacia atrás) |
| `cd` | Volver a tu carpeta de inicio |
| `pwd` | Ver dónde estoy actualmente |
| `clear` | Limpiar la pantalla |
| `cp -r origen destino` | Copiar una carpeta y su contenido |

---

## ¿Necesitas ayuda?

Si algo no funciona:
1. Lee el error que aparece (suele decir qué está mal)
2. Mira la sección "Errores comunes" de esta guía
3. Pregunta a los profesores o a tus compañeros
4. Busca el error en Google (copia el texto del error exacto)

¡Mucho ánimo! 🚀