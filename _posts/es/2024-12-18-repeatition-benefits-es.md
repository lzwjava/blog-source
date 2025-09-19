---
audio: false
generated: false
image: false
lang: es
layout: post
title: Los Beneficios de la Repetición en la Programación
translated: true
---

```bash
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:"$HOME/Library/Python/3.9/bin":/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin
```

En este caso, evita usar la variable:

`"$HOME/Library/Python/3.9/bin"`

```bash
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin
```

La segunda versión parece un poco repetitiva con el directorio `/Users/lzwjava` apareciendo varias veces, pero es mucho más limpia y fácil de leer.

La repetición en la programación puede ser realmente beneficiosa. No siempre es necesario abstraer o simplificar todo con variables o funciones. En este caso, el directorio principal `/Users/lzwjava` no es probable que cambie con frecuencia, por lo que es perfectamente aceptable repetirlo.

Esto es similar a cómo nos referimos a los nombres de las personas: si abusamos de pronombres como "él", "ella" o "ellos", se vuelve confuso de quién estamos hablando. Los nombres en sí mismos es poco probable que cambien, y usarlos directamente puede aportar claridad.

La abstracción y la simplificación son importantes, pero en algunos casos introducen una complejidad innecesaria. A veces, la repetición es más simple y comprensible.