---
audio: false
generated: true
lang: de
layout: post
title: Fehler beim Bauen von Pycrypto
translated: true
type: note
---

Der Fehler tritt auf, weil das `pycrypto`-Paket die Python-Header-Datei `longintrepr.h` benötigt, die Teil der Python-Entwicklungsheader ist. Diese Datei fehlt in Ihrer Python-3.13-Umgebung. So beheben Sie das Problem:

### Lösung:
1. **Python-Entwicklungsheader installieren**  
   Installieren Sie das Python-3.13-Entwicklungspaket für Ihr Betriebssystem. Unter Ubuntu/Debian führen Sie aus:
   ```bash
   sudo apt-get install python3.13-dev
   ```

2. **`pycrypto` neu installieren**  
   Nach der Installation der Header versuchen Sie die Installation erneut:
   ```bash
   pip install pycrypto
   ```

---

### Alternative Empfehlungen:
**Option 1: Ersetzen Sie `pycrypto` durch `pycryptodome` (Bevorzugt)**  
`pycrypto` ist veraltet und wird nicht mehr gewartet. Wechseln Sie zur gewarteten Fork `pycryptodome`, die API-kompatibel ist:
```bash
pip uninstall pycrypto
pip install pycryptodome
```

**Option 2: Verwenden Sie eine ältere Python-Version**  
Falls die Kompatibilität es erlaubt, verwenden Sie Python ≤3.9 (wo `pycrypto` bekanntermaßen funktioniert):
```bash
# Beispiel mit pyenv
pyenv install 3.9.18
pyenv local 3.9.18
pip install -r requirements.txt
```

---

### Warum das passiert ist:
- `longintrepr.h` ist ein interner Python-Header, der für die Integer-Darstellung verwendet wird. Er ist in Python-Entwicklungspaketen enthalten, aber nicht in Standardinstallationen.
- Python 3.13 könnte strukturelle Änderungen enthalten, die veraltete Pakete wie `pycrypto` (zuletzt 2014 aktualisiert) brechen.
- Die Veraltungswarnung zeigt an, dass `pycrypto` veraltete Build-Methoden verwendet, die in neueren `pip`-Versionen nicht unterstützt werden.

### Vorbeugung:
1. **Vermeiden Sie `pycrypto`**: Verwenden Sie `pycryptodome` für Kryptografie-Bedürfnisse.
2. **Pinnen Sie Python-Versionen**: Für Legacy-Projekte verwenden Sie Python ≤3.9 in Umgebungen wie Docker/Venv.
3. **Überprüfen Sie Abhängigkeiten**: Verwenden Sie `pip check`, um inkompatible Pakete zu identifizieren.

---

Keines der von Ihnen aufgeführten Pakete (`aliyunsdkcore`, `aliyun-python-sdk-ecs`, `alibabacloud_vpc20160428`, etc.) hängt direkt von **`pycrypto`** ab.

Wenn Sie jedoch sehen, dass `pycrypto` installiert wird, könnte es eine **indirekte Abhängigkeit** eines dieser Pakete sein. Um zu überprüfen, welches Paket `pycrypto` benötigt, führen Sie aus:

```bash
pip show pycrypto
```
oder
```bash
pipdeptree | grep -i pycrypto
```

### Wahrscheinliche Ursachen:
1. **Alte oder veraltete sicherheitsrelevante Pakete** (obwohl keines in Ihrer Liste explizit `pycrypto` benötigt).
2. **Eine Legacy-Abhängigkeit** von einem Paket wie `paramiko` (SSH) oder `google-auth`, aber diese sind normalerweise zu `pycryptodome` gewechselt.

### Empfohlene Maßnahme:
1. **Ersetzen Sie `pycrypto` durch `pycryptodome`** (moderne, gewartete Fork):
   ```bash
   pip uninstall pycrypto
   pip install pycryptodome
   ```
   Einige Pakete akzeptieren `pycryptodome` als Drop-in-Ersatz.

2. **Erzwingen Sie eine Neuinstallation der Abhängigkeiten**, um sicherzustellen, dass es keine versteckten Verknüpfungen gibt:
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```

3. **Wenn `pycrypto` bestehen bleibt**, überprüfen Sie Ihre Umgebung:
   ```bash
   pipdeptree --warn silence | grep -i crypto
   ```

### Wichtige Erkenntnis:
Ihre aufgeführten Pakete hängen nicht direkt von `pycrypto` ab, aber eine andere versteckte Abhängigkeit könnte es sein. Isolieren Sie es mit `pipdeptree`, um den Verursacher zu klären. Wenn kein kritisches Paket es benötigt, **entfernen Sie `pycrypto` vollständig** – es ist veraltet und potenziell unsicher.

---

Basierend auf Ihren Logs hängt keines Ihrer **explizit aufgeführten Pakete** direkt von `pycrypto` ab. Allerdings hat eine Ihrer Abhängigkeiten eine **indirekte Abhängigkeit** davon. So identifizieren und beheben Sie es:

### 1. Identifizieren des verantwortlichen Pakets
Führen Sie diesen Befehl aus, um herauszufinden, welches Top-Level-Paket `pycrypto` benötigt:
```bash
pipdeptree --warn silence | grep -i pycrypto
```

### 2. Häufige Verdächtige in Ihrem Stack
Basierend auf Ihren Paketen sind dies die wahrscheinlichsten Kandidaten:
- **`paramiko`** (verwendet von `hcloud`, `tigeropen` oder Cloud-SDKs)
- **`google-auth`** (verwendet von Google-Cloud-Paketen)
- **`boto`** (ältere AWS-Bibliotheken)
- **`ansible`** (falls indirekt verwendet)

### 3. Sofortige Lösung: Ersetzen Sie `pycrypto`
Da `pycrypto` veraltet und in Python 3.13 kaputt ist, ersetzen Sie es durch die gewartete Fork:
```bash
pip uninstall pycrypto
pip install pycryptodome
```

### 4. Wenn die Abhängigkeit bestehen bleibt
Erzwingen Sie eine Neuinstallation aller Pakete mit Abhängigkeitsprüfungen:
```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

### 5. Überprüfen Sie die Installation
Prüfen Sie, ob `pycryptodome` die Abhängigkeit erfüllt:
```bash
python -c "from Crypto import Random; print('Success')"
```

### Warum das passiert
- `pycrypto` war eine häufige Krypto-Abhängigkeit für ältere Pakete (letztes Update: 2014)
- Python 3.13 entfernte interne Header wie `longintrepr.h`, auf die `pycrypto` angewiesen war
- Moderne Alternativen wie `cryptography` (die Sie installieren) verwenden `pycrypto` nicht

Die schnellste Lösung ist **Schritt 3** – das Ersetzen von `pycrypto` durch den API-kompatiblen `pycryptodome`. Dies behebt das Kompilierungsproblem und bewahrt gleichzeitig die Kompatibilität.