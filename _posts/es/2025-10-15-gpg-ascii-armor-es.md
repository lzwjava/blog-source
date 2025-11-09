---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Armadura ASCII de GPG Explicada
translated: true
type: note
---

En GPG (GNU Privacy Guard), "armor" se refiere a ASCII armor, un formato que codifica datos binarios de OpenPGP (como archivos cifrados, firmas o claves) en una representación basada en texto y legible para humanos. Esto es útil para transmitir datos a través de canales que solo admiten texto, como el correo electrónico, sin que se corrompan—similar a cómo funcionan uuencode o base64, pero con encabezados añadidos (por ejemplo, "-----BEGIN PGP MESSAGE-----") y sumas de comprobación para la integridad.

Puedes activarlo con la opción `--armor` (o `-a`) durante comandos como el cifrado (`gpg -a -e file.txt`) o la exportación de claves (`gpg --armor --export keyid`), lo que genera el resultado en este formato de texto "armado" en lugar de en binario crudo.

## Referencias
- [What is the armored option for in GnuPG?](https://unix.stackexchange.com/questions/623375/what-is-the-armored-option-for-in-gnupg)
- [Exchanging keys - GnuPG](https://www.gnupg.org/gph/en/manual/x56.html)
- [13. ASCII armor - Notes on OpenPGP](https://openpgp.dev/book/armor.html)
- [GPG Input and Output (Using the GNU Privacy Guard)](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Input-and-Output.html)