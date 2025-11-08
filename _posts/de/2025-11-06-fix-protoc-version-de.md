---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben Sie den Substrait-Build-Protoc-Versionsfehler
translated: true
type: note
---

### Verstehen des Fehlers

Dieser Build-Fehler tritt in der `substrait`-Crate (v0.58.0) auf, von der GreptimeDB für sprachübergreifende Abfrageplanung abhängt. Der Fehler entsteht, weil der Protobuf-Compiler (`protoc`) die Datei `substrait/algebra.proto` ablehnt, da sie "optionale" Felder in der Proto3-Syntax verwendet – ein Feature, das entweder erfordert:

- Protoc Version ≥3.21 (wo die Unterstützung stabil ist und kein spezielles Flag benötigt wird), oder
- Einen älteren Protoc (z.B. 3.15–3.20) mit dem während der Kompilierung übergebenen `--experimental_allow_proto3_optional` Flag.

Das `prost-build` Tool im Build-Skript von `substrait` übergibt dieses Flag nicht, daher geht es von einer kompatiblen Protoc-Version aus. Der `protobuf-compiler` Ihres Systems (wahrscheinlich von `apt` unter Ubuntu 22.04 oder früher, was ~3.12.4 liefert) ist zu alt und unterstützt das Flag nicht, was den Absturz verursacht.

Die GreptimeDB-Dokumentation gibt protoc ≥3.15 an, aber für diese Abhängigkeit ist effektiv ≥3.21 erforderlich.

### Schnelle Lösung: Protoc auf ≥3.21 aktualisieren

Der einfachste Weg ohne Root-Rechte ist, die offizielle Binärversion herunterzuladen und zu installieren (keine Kompilierung nötig). So geht's:

1. **Neuestes Protoc herunterladen**:
   - Gehen Sie zu [Protocol Buffers Releases](https://github.com/protocolbuffers/protobuf/releases).
   - Laden Sie das neueste `protoc-<version>-linux-x86_64.zip` herunter (z.B. `protoc-28.1-linux-x86_64.zip` oder was aktuell ist – alles ≥3.21 funktioniert).
   - Beispiel Direktlink (Version anpassen):  
     `wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip`

2. **Installieren**:
   ```
   unzip protoc-*.zip -d protoc-install
   sudo mv protoc-install/bin/protoc /usr/local/bin/
   sudo chmod +x /usr/local/bin/protoc
   rm -rf protoc-install protoc-*.zip  # Bereinigung
   ```

3. **Überprüfen**:
   ```
   protoc --version
   ```
   Sollte `libprotoc 27.3` (oder höher) ausgeben. Wenn es immer noch die alte Version ist, überprüfen Sie Ihren PATH (`echo $PATH`) – `/usr/local/bin` sollte vor `/usr/bin` kommen.

4. **Build erneut versuchen**:
   ```
   make clean  # Entfernt veraltete Ziele
   make
   ```

Dies überschreibt das System-`protoc`, ohne mit `apt`-Paketen in Konflikt zu geraten. Wenn Sie auf einer neueren Distribution wie Ubuntu 24.04+ sind, könnte `apt install protobuf-compiler` bereits ≥3.21 liefern – überprüfen Sie zuerst Ihre Version.

### Falls Sie nicht aktualisieren können (seltene Fälle)
- Wenn Sie auf einem alten System feststecken, müssten Sie die `build.rs` von `substrait` patchen, um das Flag hinzuzufügen (über `Command::new(protoc).arg("--experimental_allow_proto3_optional")`), aber dies erfordert das Forken der Crate und das Aktualisieren von GreptimeDBs `Cargo.toml` – umständlich und nicht empfohlen.
- Alternativ bieten einige Crates ein `protobuf-src`-Feature an, um einen aktuellen Protoc zu bündeln, aber `substrait` aktiviert es nicht standardmäßig.

### Zusätzliche Tipps
- Stellen Sie andere Voraussetzungen sicher: `build-essential` (für GCC), `libc6-dev` (glibc headers).
- Wenn der Build durchläuft, aber später bei C++-Abhängigkeiten (z.B. Arrow) fehlschlägt, installieren Sie `libarrow-dev` via conda oder apt.
- Für CI/CD oder Docker: Fügen Sie den Download-Schritt zu Ihrer Umgebung hinzu.

Dies sollte das Problem beheben – `substrait` kompiliert problemlos auf modernen Setups. Wenn Sie auf ein weiteres Problem stoßen, teilen Sie `protoc --version` und Ihre Distribution mit.

[GreptimeDB Build Docs](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Protobuf Releases](https://github.com/protocolbuffers/protobuf/releases)  
[Proto3 Optional Fields](https://protobuf.dev/programming-guides/proto3/#optional)