---
audio: false
generated: true
lang: es
layout: post
title: Tipos de Datos del Esquema XML
translated: true
type: note
---

XML Schema define un rico conjunto de tipos de datos integrados que pueden utilizarse para especificar el tipo de datos permitido en elementos y atributos. Estos tipos de datos garantizan que el contenido XML se ajuste al formato y las restricciones previstos.

Los tipos de datos integrados en XML Schema se clasifican ampliamente en tipos **primitivos** y **derivados**. Los tipos derivados se basan en tipos primitivos y se crean aplicando restricciones u otras modificaciones.

**Tipos de Datos Primitivos (19 integrados):**

Estos son los tipos de datos fundamentales e indivisibles a partir de los cuales se derivan todos los demás tipos simples, tanto integrados como definidos por el usuario.

* **String:** Representa cadenas de caracteres.
* **Boolean:** Representa valores lógicos (verdadero o falso, también puede representarse como 1 o 0).
* **Decimal:** Representa números decimales de precisión arbitraria.
* **Float:** Representa números de punto flotante de 32 bits de precisión simple.
* **Double:** Representa números de punto flotante de 64 bits de precisión doble.
* **Duration:** Representa un intervalo de tiempo.
* **DateTime:** Representa un punto específico en el tiempo, incluyendo fecha y hora.
* **Time:** Representa un punto específico en el tiempo dentro de un período de 24 horas.
* **Date:** Representa una fecha calendario.
* **gYearMonth:** Representa un año y mes específicos.
* **gYear:** Representa un año específico.
* **gMonthDay:** Representa un mes y día específicos.
* **gDay:** Representa un día específico del mes.
* **gMonth:** Representa un mes específico del año.
* **HexBinary:** Representa datos binarios como valores hexadecimales.
* **Base64Binary:** Representa datos binarios codificados en Base64.
* **AnyURI:** Representa un Identificador Uniforme de Recursos (URI).
* **QName:** Representa un nombre calificado (un nombre con un prefijo de espacio de nombres).
* **NOTATION:** Representa el nombre de una notación declarada en el esquema.

**Tipos de Datos Derivados (alrededor de 25 integrados):**

Estos tipos de datos se derivan de los tipos primitivos aplicando restricciones (facetas) como longitud, rango, patrones, etc.

**Derivados de `string`:**

* `normalizedString`: Representa cadenas de caracteres donde los saltos de línea, tabulaciones y retornos de carro se reemplazan por espacios, y sin espacios iniciales o finales.
* `token`: Representa cadenas normalizadas sin espacios en blanco iniciales o finales, y sin secuencias internas de dos o más caracteres de espacio en blanco.
* `language`: Representa un identificador de lenguaje tal como lo define RFC 3066.
* `NMTOKEN`: Representa un token de nombre (puede contener letras, dígitos, puntos, guiones y guiones bajos).
* `NMTOKENS`: Representa una lista separada por espacios en blanco de `NMTOKEN`s.
* `Name`: Representa un nombre XML (debe comenzar con una letra o guion bajo, seguido de letras, dígitos, puntos, guiones o guiones bajos).
* `NCName`: Representa un nombre sin dos puntos (como `Name` pero no puede contener dos puntos).
* `ID`: Representa un identificador único dentro de un documento XML.
* `IDREF`: Representa una referencia a un valor `ID` en el mismo documento.
* `IDREFS`: Representa una lista separada por espacios en blanco de valores `IDREF`.
* `ENTITY`: Representa una referencia a una entidad no analizada declarada en un DTD (menos común en XML Schema).
* `ENTITIES`: Representa una lista separada por espacios en blanco de valores `ENTITY` (menos común en XML Schema).

**Derivados de `decimal`:**

* `integer`: Representa números enteros (sin parte fraccionaria).
* `nonPositiveInteger`: Representa enteros menores o iguales a 0.
* `negativeInteger`: Representa enteros estrictamente menores a 0.
* `long`: Representa enteros con signo de 64 bits.
* `int`: Representa enteros con signo de 32 bits.
* `short`: Representa enteros con signo de 16 bits.
* `byte`: Representa enteros con signo de 8 bits.
* `nonNegativeInteger`: Representa enteros mayores o iguales a 0.
* `unsignedLong`: Representa enteros sin signo de 64 bits.
* `unsignedInt`: Representa enteros sin signo de 32 bits.
* `unsignedShort`: Representa enteros sin signo de 16 bits.
* `unsignedByte`: Representa enteros sin signo de 8 bits.
* `positiveInteger`: Representa enteros estrictamente mayores a 0.

**Otros Tipos Derivados:**

* `dateTimeStamp` (en XML Schema 1.1): Similar a `dateTime` pero también incluye información de zona horaria.
* `yearMonthDuration` (en XML Schema 1.1): Representa una duración en años y meses.
* `dayTimeDuration` (en XML Schema 1.1): Representa una duración en días, horas, minutos y segundos.
* `precisionDecimal` (en XML Schema 1.1): Representa números decimales con precisión preservada.

**Tipos de Datos Definidos por el Usuario:**

Además de los tipos integrados, XML Schema permite definir sus propios tipos de datos simples y complejos utilizando mecanismos como:

* **Restricción:** Crear un nuevo tipo limitando el rango o formato de un tipo existente (ya sea integrado o definido por el usuario).
* **Lista:** Definir un tipo cuyos valores son secuencias de valores de otro tipo simple.
* **Unión:** Definir un tipo cuyos valores pueden provenir de los espacios de valor de dos o más otros tipos simples.

Al definir elementos y atributos en un XML Schema, se utiliza el atributo `type` para especificar a qué tipo de datos debe adherirse el contenido. Esto garantiza la validez de los datos y facilita su procesamiento.

Por ejemplo:

```xml
<xs:element name="age" type="xs:positiveInteger"/>
<xs:element name="name" type="xs:string"/>
<xs:attribute name="status" type="xs:token"/>
```

En este fragmento, el elemento `age` se define para contener un entero positivo, el elemento `name` una cadena de texto, y el atributo `status` un token (una cadena normalizada con manejo específico de espacios en blanco).

Comprender estos tipos de datos es fundamental para crear XML Schemas efectivos y bien definidos. Puede encontrar los detalles completos y las definiciones formales en la especificación W3C XML Schema Part 2: Datatypes.