---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Corrección de Fallo de Firma de Código en Xcode para Flutter
translated: true
type: note
---

Estás experimentando el fallo común de firma de código en Flutter/Xcode: Xcode/`security` no encontró identidades de firma válidas, por lo que `flutter run` no puede firmar la aplicación para un dispositivo físico. A continuación, te daré un conjunto claro y ordenado de soluciones y comandos para la resolución de problemas — elige la opción que prefieras (ejecutar en el Simulador ahora mismo, o configurar la firma para ejecutar en un dispositivo real). No pediré más información — asumiré que quieres solucionarlo ahora.

---

# Opciones rápidas (elige una)

**A — Ejecutar en el simulador (no se requiere firma de código)**
Si solo quieres ejecutar rápidamente sin lidiar con certificados:

1. Abre el Simulador: `open -a Simulator`
2. Ejecuta Flutter apuntando al simulador:
   `flutter run -d "$(xcrun simctl list devices | grep -m1 -o "iPhone.*(Simulator)" | sed 's/ (Simulator)//')"`
   O más simple: `flutter run -d iPhone-14` (reemplaza con un nombre de simulador disponible mostrado por `xcrun simctl list`).

**B — Arreglar la firma para desplegar en un dispositivo real (recomendado para pruebas en dispositivo)**
Sigue los pasos a continuación en orden.

---

# Pasos para arreglar la firma para despliegue en dispositivo

## 1) Confirmar entorno y comprobaciones básicas

Ejecuta estos comandos y toma nota de la salida:

```bash
flutter doctor -v
xcode-select --print-path
xcodebuild -version
security find-identity -p codesigning -v
xcrun simctl list devices
```

`security find-identity -p codesigning -v` debería mostrar al menos una identidad. En tu caso mostró `0 valid identities found` — por eso falla.

## 2) Usar la firma automática de Xcode (más fácil)

1. Abre el workspace:
   `open ios/Runner.xcworkspace`
2. En Xcode: selecciona el proyecto `Runner` → target `Runner` → **Signing & Capabilities**.
3. Establece **Team** a tu Apple ID / cuenta de Apple Developer. Si tu Apple ID no está añadido:

   * Xcode → Preferences → Accounts → `+` → añade Apple ID.
4. Marca **Automatically manage signing**.
5. Asegúrate de que el **Bundle Identifier** es único (estilo DNS inverso, ej. `com.tunombre.tuaplicacion`).
6. Xcode intentará crear un certificado de desarrollo y un perfil de provisionamiento; si ves prompts, permite que Xcode lo gestione.

> Nota: Para el despliegue completo en un dispositivo arbitrario necesitas una membresía de Apple Developer ($99/año). Xcode puede usar un Apple ID gratuito para "free provisioning", pero es limitado (número de dispositivos, sin ciertos entitlements).

## 3) Registrar tu dispositivo (si es requerido)

Si Xcode no puede registrar tu dispositivo automáticamente, ve al Apple Developer Portal → Certificates, IDs & Profiles → Devices → añade el UDID del dispositivo. Puedes obtener el UDID del dispositivo conectándolo y seleccionándolo en la ventana Devices and Simulators de Xcode.

## 4) Generar/importar certificado manualmente (si ya tienes un p12)

Si tienes un certificado `.p12` y una clave privada:

```bash
security import /ruta/al/certificado.p12 -k ~/Library/Keychains/login.keychain-db -P "CONTRASEÑA_P12" -T /usr/bin/codesign
```

Luego vuelve a ejecutar `security find-identity -p codesigning -v` para confirmar que aparece.

## 5) Si prefieres que Xcode cree certificados por ti

En Xcode → Accounts → Selecciona tu Apple ID → Manage Certificates → `+` → añade **iOS Development**. Esto crea un certificado en tu llavero y aparecerá en `security find-identity`.

## 6) Asegúrate de que Command Line Tools esté configurado

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

Luego acepta la licencia si es necesario:

```bash
sudo xcodebuild -license accept
```

## 7) Después de configurar la firma, ejecuta desde la terminal

Desde la raíz del proyecto:

```bash
flutter clean
flutter pub get
flutter run
```

Si hay múltiples dispositivos, especifica `-d <id-del-dispositivo>`.

---

# Consejos para resolución de problemas y errores comunes

* **Persiste "0 valid identities found"** — confirma que la clave privada del certificado está en el llavero de inicio (abre Keychain Access → login). Si importaste el certificado pero no la clave privada, la firma falla.
* **Bundle ID no coincide** — el App ID en el Developer Portal debe coincidir exactamente con el bundle identifier en Xcode (se permiten wildcards para algunos casos).
* **Team no seleccionado** — Xcode muestra "No account" — añade Apple ID en Xcode Preferences → Accounts.
* **Perfil de provisionamiento caducado** — revisa el Developer Portal y regenera el perfil de provisionamiento.
* **Limitaciones del free provisioning** — si usas un Apple ID gratuito, puede que necesites re-provisionar cada 7 días y tienes dispositivos limitados.
* **CI / automatización** — usa `fastlane match` o las APIs de App Store Connect para gestionar certificados y perfiles centralmente.
* **Errores de permisos de Codesign** — asegúrate de que el elemento del Llavero otorga acceso a codesign; a veces debes permitir manualmente a `/usr/bin/codesign` acceder a la clave privada en el Llavero.
* **Si `flutter run` aún falla**, ejecuta la build de Xcode para ver un error más detallado: abre el workspace y presiona Run en Xcode; revisa los errores de Signing & Capabilities en la UI.

---

# Comandos útiles para copiar y pegar

Listar identidades de firma de código:

```bash
security find-identity -p codesigning -v
```

Importar `.p12`:

```bash
security import /ruta/a/tucertificado.p12 -k ~/Library/Keychains/login.keychain-db -P "CONTRASEÑAP12" -T /usr/bin/codesign
```

Establecer las herramientas de línea de comandos de Xcode:

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

Abrir el workspace de iOS:

```bash
open ios/Runner.xcworkspace
```

---

# Si quieres, puedo

* dar la secuencia exacta de clics en Xcode para crear certificado/perfil paso a paso (ya incluí los pasos principales), o
* proporcionar comandos de ejemplo de `fastlane`/`match` si quieres automatización para múltiples máquinas/CI, o
* ayudar a interpretar cualquier nuevo error después de que pruebes la ruta de firma automática de Xcode.

Dime qué ruta elegiste (Simulador ahora / Xcode automático / importación manual de p12 / CI) y pega cualquier nuevo error si aún falla — te daré los siguientes pasos.