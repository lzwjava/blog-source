---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Instalación y Uso de GraalVM
translated: true
type: note
---

## ¿Qué es GraalVM?

GraalVM es un entorno de ejecución de alto rendimiento de código abierto (distribución de JDK) que admite múltiples lenguajes de programación como Java, JavaScript, Python y más. Cuenta con un compilador JIT avanzado para una ejecución más rápida y la capacidad de compilar aplicaciones Java a ejecutables nativos a través de Native Image, reduciendo el tiempo de inicio y la huella de memoria.

## Instalación

1. **Descargar GraalVM**:
   - Ve a la página oficial de descargas de GraalVM.
   - Elige la Community Edition (gratuita) u Oracle GraalVM (con funciones adicionales).
   - Selecciona la versión para tu plataforma (por ejemplo, Linux, macOS, Windows) y arquitectura (x64 o ARM).
   - A partir de 2025, la última versión estable es GraalVM para JDK 22 o 23—consulta el sitio para la más actual.

2. **Extraer e Instalar**:
   - Descomprime el archivo descargado en un directorio, por ejemplo, `/opt/graalvm` en Linux/macOS o `C:\Program Files\GraalVM` en Windows.
   - No se necesita instalador; es una distribución portable.

3. **Configurar Variables de Entorno**:
   - Establece `JAVA_HOME` en el directorio de GraalVM (por ejemplo, `export JAVA_HOME=/opt/graalvm` en Linux/macOS).
   - Añade el directorio `bin` a tu `PATH` (por ejemplo, `export PATH=$JAVA_HOME/bin:$PATH`).
   - Verifica con `java -version`; debería mostrar los detalles de GraalVM.

4. **Instalar Componentes Adicionales (Opcional)**:
   - Usa `gu` (GraalVM Updater) para entornos de ejecución de lenguajes o Native Image: `gu install native-image` (requiere herramientas de compilación como `build-essential` en Linux).

## Construyendo un Programa Hola Mundo

Usaremos Java para este ejemplo, ya que es el lenguaje principal de GraalVM. Crea una aplicación simple "Hola Mundo", compílala y ejecútala.

### Paso 1: Escribir el Código
Crea un archivo llamado `HelloWorld.java`:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from GraalVM!");
    }
}
```

### Paso 2: Compilar
Abre una terminal en el directorio con el archivo y ejecuta:
```
javac HelloWorld.java
```
Esto produce `HelloWorld.class`.

### Paso 3: Ejecutar
```
java HelloWorld
```
Salida:
```
Hello, World from GraalVM!
```

### Avanzado: Compilar a Ejecutable Nativo
La función Native Image de GraalVM te permite construir un binario independiente.

1. Asegúrate de que Native Image esté instalado: `gu install native-image`.
2. Genera una configuración (la primera ejecución puede requerir esto):
   ```
   native-image --no-fallback -H:+ReportExceptionStackTraces HelloWorld
   ```
   - Esto crea `HelloWorld` (o `helloworld.exe` en Windows), un binario nativo.
   - En la primera compilación, analiza la aplicación y puede tardar unos minutos.

3. Ejecuta el binario nativo:
   ```
   ./HelloWorld
   ```
   La salida es la misma, pero se inicia instantáneamente con un uso bajo de memoria.

## Consejos para Usar GraalVM
- **Cambiar entre JDKs**: Usa SDKMAN! (`sdk install java 22.0.2-graal`) para una gestión fácil.
- **Multilenguaje**: Ejecuta código Node.js con `node` desde GraalVM, o Python con `python`.
- **Rendimiento**: Habilita el JIT de GraalVM con `-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler`.
- **Resolución de Problemas**: Revisa los registros en `~/.gu/` para problemas; asegúrate de que tu sistema tenga un compilador C para Native Image.

Para más detalles, consulta la documentación oficial.

[Descargas de GraalVM](https://www.graalvm.org/downloads/)  
[Guía de Usuario de GraalVM](https://www.graalvm.org/latest/reference-manual/)  
[Tutorial de Native Image](https://www.graalvm.org/latest/reference-manual/native-image/)