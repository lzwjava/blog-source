---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Cómo Resolver el Bloqueo de Flutter Clean en macOS
translated: true
type: note
---

Ah, ya veo lo que quieres decir 👍  
A veces `flutter clean` puede parecer que se "cuelga" en macOS — especialmente si hay muchos archivos generados, o si las carpetas `DerivedData` de Xcode son muy grandes.

---

### ✅ Prueba Estos Pasos

1. **Cancela el comando atascado**  
   Presiona `CTRL + C`.

2. **Limpia manualmente (mismo efecto que `flutter clean`)**  
   Puedes eliminar estas carpetas de build/cache tú mismo:
   ```bash
   rm -rf build/ .dart_tool/ ios/Pods ios/Podfile.lock ios/Flutter/Flutter.framework ios/Flutter/Flutter.podspec
   ```

   Si también quieres eliminar la caché de Xcode:
   ```bash
   rm -rf ~/Library/Developer/Xcode/DerivedData
   ```

3. **Vuelve a obtener las dependencias**
   ```bash
   flutter pub get
   ```

4. **Reinstala CocoaPods (para iOS)**
   ```bash
   cd ios
   pod install --repo-update
   cd ..
   ```

5. **Compila/ejecuta de nuevo**
   ```bash
   flutter run
   ```

---

⚡ **Tip:** La primera vez después de limpiar puede tomar un poco más de tiempo (ya que Flutter necesita regenerar `.dart_tool`, `.pub-cache`, los Pods de iOS, etc.), pero no debería quedarse congelado para siempre. Si sigues viendo que se "atasca", podría estar relacionado con:

- **Flutter SDK desactualizado** → Ejecuta `flutter upgrade`
- **CocoaPods desactualizado** → Ejecuta `sudo gem install cocoapods`  
- **Problemas con Rosetta / chip M1**: Si estás en Apple Silicon, a veces necesitas ejecutar `arch -x86_64 pod install` dentro de la carpeta `ios`, dependiendo de tu configuración.

---

👉 ¿Quieres que te dé un **script de una sola línea** que borre las cachés de build y reinicie los Pods (básicamente un "super clean") para que no tengas que depurar cuando `flutter clean` se atasque?