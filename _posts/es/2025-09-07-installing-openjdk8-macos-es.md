---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Instalación de OpenJDK 8 en macOS
translated: true
type: note
---

Aquí te mostramos cómo instalar **OpenJDK 8** (Java SE 8) en macOS en **2025**, con métodos que cubren Homebrew, SDKMAN, instaladores manuales y MacPorts. Sin tablas, solo flujos claros y sencillos:

---

## 1. Usando Homebrew (`openjdk@8`)

Esta sigue siendo una de las formas más simples de instalar OpenJDK 8 en macOS.

### Pasos:

1. Abre Terminal.

2. Ejecuta:

   ```bash
   brew install openjdk@8
   ```

   ([Homebrew Formulae][1])

3. Después de la instalación, enlaza el JDK para que las herramientas de macOS puedan detectarlo:

   ```bash
   sudo ln -sfn $(brew --prefix)/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-8.jdk
   ```

   ([Homebrew Formulae][1])

4. Opcionalmente, añade OpenJDK 8 a tu PATH en tu configuración de shell (por ejemplo, `.zshrc`):

   ```bash
   export PATH="$(brew --prefix openjdk@8)/bin:$PATH"
   ```

**Nota para usuarios de Apple Silicon (serie M):**
Si enfrentas problemas de arquitectura, podrías necesitar ejecutar Homebrew bajo Rosetta 2:

```bash
env /usr/bin/arch -x86_64 /bin/zsh --login
brew install openjdk@8
```

Luego procede con la configuración del enlace simbólico y el PATH ([Stack Overflow][2]).

---

## 2. Vía SDKMAN (gestor de versiones de Java)

SDKMAN es una herramienta flexible para instalar y cambiar entre múltiples versiones de Java.

### Instalación rápida:

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk list java
sdk install java 8.xxx-tem
```

Reemplaza `8.xxx-tem` con el identificador mostrado en `sdk list java`. ([Stack Overflow][2])

---

## 3. Instalación Manual (Oracle / Adoptium / AdoptOpenJDK)

### Opción A: Instalador .dmg / .pkg de Oracle

1. Descarga el instalador correcto para tu arquitectura desde la página de descarga de Java SE 8 de Oracle.
2. Abre el `.dmg`, ejecuta el instalador `.pkg` y sigue las instrucciones. ([Documentación de Oracle][3])
3. Una vez instalado, usa herramientas como `java_home` para elegir la versión:

   ```bash
   /usr/libexec/java_home -v 1.8 --exec java -version
   ```

### Opción B: AdoptOpenJDK o builds similares

AdoptOpenJDK (ahora bajo Eclipse Adoptium) proporciona builds, con opciones tanto de instalador como de archivo.

* Por ejemplo, la documentación de Salesforce en agosto de 2025 sugiere usar el sitio de AdoptOpenJDK, eligiendo OpenJDK 8 (LTS) con la JVM HotSpot, y proceder a través de su instalador. ([Salesforce][4])

Después de instalar, configura tu JAVA\_HOME, por ejemplo:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
export PATH=$JAVA_HOME/bin:$PATH
```

---

## 4. MacPorts

Si usas MacPorts en lugar de Homebrew, instalar OpenJDK 8 es sencillo:

```bash
sudo port install openjdk8
```

Para ver qué está instalado:

```bash
port contents openjdk8
```

Para actualizar después:

```bash
sudo port selfupdate && sudo port upgrade openjdk8
```

([MacPorts][5])

---

## Cómo Elegir el Método Correcto para Ti

| Intención                                             | Mejor Método                                    |
| ----------------------------------------------------- | ----------------------------------------------- |
| Instalación rápida y mantenimiento fácil              | **Homebrew (`brew install openjdk@8`)**         |
| Gestionar múltiples versiones de Java concurrentes    | **SDKMAN**                                      |
| Control total e instalador oficial (amigable con GUI) | **Manual `.dmg` o `.pkg** vía Oracle/Adoptium   |
| Preferencia por el ecosistema MacPorts                | **MacPorts**                                    |

---

## Verificando la Instalación

Después de la instalación, compruébalo con:

```bash
java -version
```

Espera algo como `"1.8.0_xxx"` para confirmar que Java 8 está activo. Para un control preciso:

```bash
/usr/libexec/java_home -v 1.8 --exec javac -version
```

---

## Reflexiones Finales

En resumen:

* **Homebrew** es la opción más popular en 2025: solo `brew install openjdk@8`, luego enlaza y configura el PATH.
* **SDKMAN** te da flexibilidad si cambias de versión de Java frecuentemente.
* **Los instaladores manuales** (Oracle, Adoptium) siguen siendo una opción sólida y basada en GUI.
* **MacPorts** funciona si ese es tu gestor de paquetes preferido.

¡Avísame si necesitas ayuda para configurar tu shell, cambiar entre versiones de Java o cualquier otra cosa en el proceso!

[1]: https://formulae.brew.sh/formula/openjdk%408?utm_source=chatgpt.com "openjdk@8"
[2]: https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac?utm_source=chatgpt.com "How to install Java 8 on Mac"
[3]: https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html?utm_source=chatgpt.com "JDK 8 Installation for macOS"
[4]: https://help.salesforce.com/s/articleView?id=001117155&language=en_US&type=1&utm_source=chatgpt.com "How to Install OpenJDK 8 on macOS to Work with Anypoint ..."
[5]: https://ports.macports.org/port/openjdk8/?utm_source=chatgpt.com "Install openjdk8 on macOS with MacPorts"