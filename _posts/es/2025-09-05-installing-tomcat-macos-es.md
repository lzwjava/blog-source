---
audio: false
generated: true
image: false
lang: es
layout: post
title: Instalación de Apache Tomcat en macOS
translated: true
type: note
---

Aquí tienes una guía paso a paso para instalar y ejecutar **Apache Tomcat en macOS**:

---

### 1. Verificar Java

Tomcat requiere Java. Verifica que lo tienes instalado:

```bash
java -version
```

Si no ves una versión de Java (por ejemplo, `1.8`, `11` o superior), instálala. En macOS, la forma más fácil es mediante [Homebrew](https://brew.sh):

```bash
brew install openjdk@11
```

Luego enlázala:

```bash
brew link --force --overwrite openjdk@11
```

---

### 2. Instalar Tomcat (Opción A: Homebrew – la más fácil)

Con Homebrew puedes instalar Tomcat rápidamente:

```bash
brew install tomcat
```

Esto normalmente instala la última versión (por ejemplo, Tomcat 10).

La encontrarás en:

```
/usr/local/Cellar/tomcat/<version>/libexec
```

O si usas Apple Silicon:

```
/opt/homebrew/Cellar/tomcat/<version>/libexec
```

Ejecútala con:

```bash
catalina run
```

---

### 3. Instalar Tomcat (Opción B: Descarga Manual – la forma oficial)

1. Ve al [sitio web de Apache Tomcat](https://tomcat.apache.org/download-10.cgi) y descarga la última versión estable (elige el `.tar.gz`).

2. Extráelo en un directorio, por ejemplo:

   ```bash
   tar xvf apache-tomcat-10.*.tar.gz
   mv apache-tomcat-10.* ~/tomcat
   ```

3. Inicia Tomcat:

   ```bash
   cd ~/tomcat/bin
   ./startup.sh
   ```

4. Para detenerlo:

   ```bash
   ./shutdown.sh
   ```

---

### 4. Verificar la Instalación

Abre tu navegador y ve a:

```
http://localhost:8080
```

Deberías ver la página de bienvenida de Tomcat.

---

### 5. (Opcional) Agregar al PATH

Para poder ejecutar `startup.sh` desde cualquier lugar, agrega esto a tu `~/.zshrc` o `~/.bashrc`:

```bash
export CATALINA_HOME=~/tomcat
export PATH=$CATALINA_HOME/bin:$PATH
```

Recarga:

```bash
source ~/.zshrc
```

---

👉 Eso es todo. Ahora tienes Tomcat ejecutándose localmente en macOS.

¿Quieres que también te muestre **cómo desplegar un archivo WAR en Tomcat en macOS** después de la configuración?