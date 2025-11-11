---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Corrección de la Discrepancia de Ruby en CocoaPod en macOS
translated: true
type: note
---

Veo lo que está pasando: tu configuración de Ruby y gems está un poco mezclada, por lo que el comando `pod deintegrate` no puede encontrar CocoaPods. Vamos a resolverlo paso a paso:

---

### Problema
- Estás en macOS (probablemente `arm64`, M1/M2).
- Actualizaste Ruby (a 3.4.1 via Homebrew).
- Tu ejecutable `pod` pertenece a la versión anterior de Ruby (ruta de gems de 3.3.0: `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`).
- Pero ahora Ruby 3.4.1 está activo, por lo que no puede encontrar los gems `cocoapods` en la ubicación correcta.

Esa discrepancia es la razón por la que está fallando.

---

### Soluciones

#### 1. Reinstalar CocoaPods usando la versión de Ruby que estás ejecutando actualmente
```bash
gem install cocoapods
```

Luego verifica con:
```bash
which pod
pod --version
```

---

#### 2. Si estás usando Ruby de `brew`, es mejor instalar CocoaPods via Homebrew también
```bash
brew install cocoapods
```

Esto evita completamente los conflictos de versiones de Ruby.

---

#### 3. Si estás usando `rbenv` o `rvm`, asegúrate de estar en el entorno de la versión correcta de Ruby
Por ejemplo, con `rbenv`:
```bash
rbenv global 3.4.1
gem install cocoapods
```

---

#### 4. Limpiar los enlaces simbólicos antiguos del binario pod
Verifica de dónde viene el comando `pod` huérfano:
```bash
which pod
```
Si apunta a `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`, elimínalo o actualiza tu `PATH` para que use el correcto.

---

✅ Recomendado (fácil y estable): Simplemente ejecuta   
```bash
brew install cocoapods
```
y luego vuelve a intentar:
```bash
pod deintegrate
```

---

¿Quieres que te ayude a **arreglar el PATH para que siempre seleccione el binario pod correcto**, o prefieres solo la reinstalación rápida?