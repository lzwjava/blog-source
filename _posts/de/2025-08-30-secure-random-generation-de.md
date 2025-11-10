---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Sichere Zufallsgenerierung mit Python Secrets
translated: true
type: note
---

### Einführung in das `secrets`-Modul

Das `secrets`-Modul (eingeführt in Python 3.6) ist Teil der Standardbibliothek und bietet Zugriff auf kryptografisch starke Zufallszahlengenerierung. Im Gegensatz zum `random`-Modul, das für Simulationen oder Spiele geeignet ist, ist `secrets` für sicherheitsrelevante Aufgaben wie das Generieren von Passwörtern, Tokens oder Geheimnissen konzipiert, da es den kryptografisch sicheren Zufallszahlengenerator des Betriebssystems verwendet (z. B. `/dev/urandom` auf Unix-ähnlichen Systemen).

Um es zu verwenden, importieren Sie es einfach:
```python
import secrets
```

### Wichtige Funktionen und Verwendung

Hier sind die Hauptfunktionen in `secrets` mit kurzen Erklärungen und Beispielen. Diese generieren Zufallswerte, die schwer vorhersehbar sind.

| Funktion | Zweck | Beispielverwendung |
|----------|---------|---------------|
| `secrets.token_bytes(n)` | Generiert `n` zufällige Bytes. Nützlich zum Erstellen binärer Schlüssel. | `key = secrets.token_bytes(16)`  # 16 zufällige Bytes |
| `secrets.token_hex(n)` | Generiert `n` zufällige Bytes und gibt sie als Hex-String zurück (doppelt so lang wie `n` aufgrund der Hex-Kodierung). Ideal für hexadezimale Tokens. | `hex_key = secrets.token_hex(16)`  # 32-stelliger Hex-String |
| `secrets.token_urlsafe(n)` | Generiert `n` zufällige Bytes, base64-kodiert für URL-sichere Verwendung (z. B. in Web-Tokens). | `url_token = secrets.token_urlsafe(32)`  # ~43-stelliger String |
| `secrets.randbelow(n)` | Gibt eine zufällige Ganzzahl zwischen 0 und `n-1` (inklusive) zurück. Sichere Alternative zu `random.randint`. | `num = secrets.randbelow(100)`  # Zufällige Ganzzahl von 0 bis 99 |
| `secrets.choice(seq)` | Gibt ein zufälliges Element aus einer nicht-leeren Sequenz `seq` zurück. Sichere Alternative zu `random.choice`. | `item = secrets.choice(['a', 'b', 'c'])`  # Zufällig aus der Liste |

### Praktische Beispiele

1. **Generieren eines sicheren Passworts**:
   Kombinieren Sie `secrets.choice` mit String-Konstanten für ein zufälliges Passwort.
   ```python
   import string
   import secrets

   alphabet = string.ascii_letters + string.digits + string.punctuation
   password = ''.join(secrets.choice(alphabet) for _ in range(12))
   print(password)  # z. B. "X8f#9L&pW2c%"
   ```

2. **Erstellen von API-Tokens**:
   Verwenden Sie `token_urlsafe` für websichere Zufallsstrings.
   ```python
   token = secrets.token_urlsafe(32)
   print(token)  # z. B. "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
   ```

3. **Zufällige Auswahl für Spiele oder Simulationen (mit Sicherheit)**:
   ```python
   winners = secrets.choice(['Alice', 'Bob', 'Charlie'])
   print(f"Gewinner: {winners}")
   ```

### Best Practices und Hinweise

- **Sicherheitsbegründung**: `secrets` vermeidet Vorhersehbarkeit und ist resistent gegen Angriffe. Verwenden Sie niemals `random` für Passwörter oder Tokens, da es geseedet und vorhergesagt werden kann.
- **Leistung**: Aufrufe können langsamer sein als bei `random`, aber das ist in Ordnung für sicherheitskritischen Code – verwenden Sie es nicht übermäßig in Schleifen für nicht-kritische Aufgaben.
- **Randfälle**: `secrets.choice` löst einen `ValueError` für leere Sequenzen aus; `randbelow(0)` löst einen `ValueError` aus.
- **Abhängigkeiten**: Keine externen Bibliotheken erforderlich; es ist integriert.
- Für weitere Details lesen Sie die [offiziellen Python-Dokumente](https://docs.python.org/3/library/secrets.html). Wenn Sie einen spezifischen Anwendungsfall haben, geben Sie mehr Kontext für maßgeschneiderte Ratschläge!