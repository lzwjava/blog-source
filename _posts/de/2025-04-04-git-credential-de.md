---
audio: false
generated: true
lang: de
layout: post
title: Git-Anmeldeinformationsverwaltung
translated: true
type: note
---

Sie verwenden **Git Credential Manager (GCM) Version 2.6.1** auf **macOS** und sind auf ein Problem gestoßen, bei dem `git config --global credential.helper manager-core` einen Fehler verursacht:

```
warning: credential.helper has multiple values
error: cannot overwrite multiple values with a single value
```

Dies passiert, weil bereits mehrere Credential-Helper in Ihrer Git-Konfiguration gesetzt sind. Sie müssen **die vorhandenen Werte löschen**, bevor Sie einen neuen setzen.

---

### **🛠 Das Problem beheben: Credential-Helper zurücksetzen**
#### **Schritt 1: Aktuelle Credential-Helper überprüfen**
Führen Sie aus:
```sh
git config --global --get-all credential.helper
```
Dies listet alle konfigurierten Credential-Helper auf.

#### **Schritt 2: Vorherige Credential-Helper entfernen**
Setzen Sie alle Credential-Helper zurück mit:
```sh
git config --global --unset-all credential.helper
```

#### **Schritt 3: GCM als einzigen Credential-Helper setzen**
Setzen Sie nun **Git Credential Manager (GCM)** wieder als Helper:
```sh
git config --global credential.helper manager-core
```

#### **Schritt 4: Die Änderung überprüfen**
Prüfen Sie, ob es korrekt gesetzt ist:
```sh
git config --global --get credential.helper
```
Erwartete Ausgabe:
```
manager-core
```

---

### **🛠 Alternative: `--replace-all` verwenden**
Wenn Sie vorhandene Werte überschreiben möchten, ohne sie zuerst zu entfernen, verwenden Sie:
```sh
git config --global --replace-all credential.helper manager-core
```

---

### **🧩 Zusätzliche Fehlerbehebung**
Wenn Sie immer noch Probleme haben, können Sie Ihre vollständige globale Git-Konfiguration überprüfen:
```sh
git config --global --list
```
Wenn das Problem weiterhin besteht, lassen Sie es mich wissen! 🚀

---

Git Credential Manager (GCM) ist ein sicherer Git Credential-Helper, der Authentifizierungsdaten für HTTPS-Git-Repositories speichert und verwaltet. Er funktioniert mit Diensten wie GitHub, GitLab, Bitbucket und Azure DevOps.

---

## **1. Git Credential Manager installieren**
GCM ist in Git für Windows und den offiziellen Git-Distributionen für macOS und Linux enthalten. Wenn es nicht installiert ist, laden Sie es hier herunter:

🔗 **[Git Credential Manager auf GitHub](https://github.com/GitCredentialManager/git-credential-manager)**

### **Überprüfen, ob GCM installiert ist**
Führen Sie aus:
```sh
git credential-manager version
```
Wenn es installiert ist, sehen Sie eine Versionsnummer. Wenn nicht, installieren Sie es manuell.

---

## **2. Git für die Verwendung von GCM konfigurieren**
Führen Sie den folgenden Befehl aus:
```sh
git config --global credential.helper manager
```
Für macOS/Linux verwenden Sie:
```sh
git config --global credential.helper manager-core
```

Um den aktuellen Credential-Helper zu überprüfen:
```sh
git config --global credential.helper
```

---

## **3. Bei einem Git-Server authentifizieren**
Sobald es konfiguriert ist, wird GCM Sie beim ersten Interagieren mit einem Remote-Repository über HTTPS (z.B. `git clone`, `git pull`) zur Eingabe von Anmeldedaten auffordern.

- Bei Verwendung von GitHub, GitLab oder Bitbucket öffnet GCM einen Browser für die OAuth-Authentifizierung.
- Wenn Sie ein Personal Access Token (PAT) verwenden, geben Sie dieses anstelle eines Passworts ein.

---

## **4. Anmeldedaten speichern und verwalten**
GCM speichert Anmeldedaten sicher im Credential-Speicher des Betriebssystems:
- **Windows**: Windows Credential Manager
- **macOS**: macOS Keychain
- **Linux**: GPG-verschlüsselte Datei (`~/.git-credentials` oder `~/.gitconfig`)

Um eine Anmeldeinformation manuell hinzuzufügen:
```sh
git credential approve
```

Um eine gespeicherte Anmeldeinformation zu entfernen:
```sh
git credential reject https://github.com
```

Um alle Anmeldedaten zu löschen:
```sh
git credential reject
```

---

## **5. Git Credential Manager mit verschiedenen Git-Anbietern verwenden**
### **GitHub**
Verwenden Sie ein **Personal Access Token (PAT)** anstelle eines Passworts:
```sh
git credential reject https://github.com
git pull
```
Sie werden aufgefordert, sich anzumelden und Ihr Token einzugeben.

### **GitLab**
Für GitLab verwenden Sie OAuth oder ein **PAT**:
```sh
git credential reject https://gitlab.com
git pull
```

### **Azure DevOps**
Verwenden Sie ein **PAT** oder die Azure-Authentifizierung.

---

## **6. Probleme beheben**
Wenn Anmeldedaten nicht korrekt gespeichert oder abgerufen werden:
1. Überprüfen Sie den Credential-Helper:
   ```sh
   git config --global credential.helper
   ```
2. Setzen Sie den Git Credential Manager zurück:
   ```sh
   git credential reject https://your-git-service.com
   ```
3. Installieren Sie GCM bei Bedarf neu.

Benötigen Sie Hilfe bei der Konfiguration für einen bestimmten Dienst? 🚀