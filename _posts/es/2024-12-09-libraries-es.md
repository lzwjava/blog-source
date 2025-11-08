---
audio: false
generated: false
image: false
lang: es
layout: post
title: Considera Actualizaciones al Usar Bibliotecas
translated: true
type: post
---

Utilicé CodeIgniter en mi proyecto de startup, [Fun Live](https://github.com/lzwjava/live-server). Aunque el proyecto terminó, después de varios años, quise revivirlo para conmemorarlo. Sin embargo, en 2016, usé CodeIgniter 3, mientras que la versión más reciente ahora es CodeIgniter 4.

La actualización ha demostrado ser problemática porque mi código está estrechamente acoplado con el framework CodeIgniter. Siguiendo la guía de actualización en [https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html), se evidencia que se requiere un esfuerzo significativo para actualizar la base de código.

Esta experiencia me enseñó una lección importante: al escribir código, debemos considerar cuidadosamente cómo manejar futuras actualizaciones. Es crucial pensar en qué partes del código controlamos y cuáles están controladas por dependencias de terceros.