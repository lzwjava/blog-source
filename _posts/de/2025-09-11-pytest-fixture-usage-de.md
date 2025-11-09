---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Verständnis der Pytest-Fixture-Nutzung
translated: true
type: note
---

## Was ist `@pytest.fixture`?

`@pytest.fixture` ist ein Dekorator, der eine Funktion als **Fixture** kennzeichnet – eine spezielle Funktion, die Testdaten, Setup- oder Teardown-Funktionalität für Ihre Tests bereitstellt. Fixtures sind eine der leistungsstärksten Funktionen von pytest und ein Hauptgrund, warum viele Entwickler pytest gegenüber Pythons eingebautem `unittest`-Modul bevorzugen.

## Wie Fixtures funktionieren

Fixtures folgen einem einfachen, aber leistungsstarken Muster:

1. **Setup**: Der Code vor der `yield`-Anweisung läuft vor dem Test
2. **Testausführung**: Der Test läuft, wenn er die `yield`-Anweisung erreicht
3. **Teardown**: Der Code nach der `yield`-Anweisung läuft nach Abschluss des Tests

### Einfaches Fixture-Beispiel

```python
import pytest

@pytest.fixture
def sample_data():
    # Setup-Code
    data = {"name": "John", "age": 30}
    yield data  # Test läuft hier
    # Teardown-Code (läuft nach dem Test)
    print("Cleaning up sample data")
```

## Warum wir Fixtures benötigen

Fixtures lösen mehrere häufige Testprobleme:

1. **Testisolation**: Stellen sicher, dass jeder Test mit frischen, vorhersehbaren Daten läuft
2. **Codewiederverwendung**: Vermeiden Sie die Wiederholung von Setup-/Teardown-Code über mehrere Tests hinweg
3. **Ressourcenverwaltung**: Korrektes Handhaben von Ressourcen wie Datenbankverbindungen, Dateien oder Netzwerkverbindungen
4. **Testklarheit**: Halten Sie Testfunktionen auf das fokussiert, was sie testen, nicht auf das Setup
5. **Dependency Injection**: Stellen Sie genau das bereit, was jeder Test benötigt

## Wichtige Merkmale von Fixtures

### 1. Dependency Injection

Fixtures können von anderen Fixtures abhängen und erstellen einen Abhängigkeitsgraphen:

```python
@pytest.fixture
def database_connection():
    # Datenbankverbindung einrichten
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database_connection):
    # Verwendet die database_connection-Fixture
    create_table(database_connection, "users")
    yield
    drop_table(database_connection, "users")
```

### 2. Scope-Kontrolle

Fixtures können unterschiedliche Lebensdauern haben:

```python
@pytest.fixture(scope="function")  # Standard - läuft einmal pro Test
def per_test_fixture():
    pass

@pytest.fixture(scope="module")  # Läuft einmal pro Modul
def per_module_fixture():
    pass

@pytest.fixture(scope="session")  # Läuft einmal pro Test-Session
def per_session_fixture():
    pass
```

### 3. Autouse-Fixtures

Fixtures können automatisch ausgeführt werden, ohne angefordert zu werden:

```python
@pytest.fixture(autouse=True)
def always_run_this():
    # Dies läuft vor jedem Test im Modul
    yield
    # Dies läuft nach jedem Test
```

### 4. Parametrisierte Fixtures

Fixtures können mehrere Datensätze generieren:

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param  # Führt Tests mit 1, 2 und 3 aus
```

## Praktisches Beispiel mit API-Tests

So helfen Fixtures bei Ihrem Finanz-Header-Testszenario:

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # Setup - Header erstellen
    headers = create_financial_header()  # Ihre Erstellungslogik
    yield headers  # Test läuft hier mit diesen Headern

    # Teardown - Header löschen
    delete_financial_header(headers)  # Ihre Aufräumlogik

def test_submit_transaction(financial_header):
    # Die Fixture stellt die Header automatisch bereit
    response = requests.post(
        "https://api.example.com/transactions",
        headers=financial_header,
        json={"amount": 100}
    )
    assert response.status_code == 201

def test_validate_header(financial_header):
    # Dieselbe Fixture wird in einem anderen Test verwendet
    response = requests.get(
        "https://api.example.com/validate",
        headers=financial_header
    )
    assert response.json()["valid"] is True
```

## Vergleich mit unittest

| Merkmal               | pytest Fixtures                     | unittest setUp/tearDown          |
|-----------------------|-------------------------------------|----------------------------------|
| Dependency Injection  | ✅ Ja                               | ❌ Nein                          |
| Scope-Kontrolle       | ✅ Funktion, Klasse, Modul, Session | ❌ Nur Methoden-/Klassenebene    |
| Saubere Syntax        | ✅ Einfacher Dekorator              | ❌ Erfordert Vererbung           |
| Testisolation         | ✅ Jeder Test erhält frische Fixtures | ❌ Gemeinsamer Zustand kann Probleme verursachen |
| Parametrisierung      | ✅ Eingebaute Unterstützung         | ❌ Manuelle Implementierung erforderlich |

## Wann Fixtures verwendet werden sollten

Verwenden Sie Fixtures, wenn Sie benötigen:
- Testdaten oder -objekte einzurichten
- Externe Ressourcen zu verwalten (DB-Verbindungen, Dateien usw.)
- Aufräumarbeiten nach Tests durchzuführen
- Gemeinsame Testabhängigkeiten zu teilen
- Verschiedene Testumgebungen zu erstellen
- Komplexe Setup-/Teardown-Logik zu implementieren

Fixtures sind besonders wertvoll beim API-Testing (wie in Ihrem Finanz-Header-Fall), weil sie helfen, den Lebenszyklus von Testressourcen sauber und vorhersehbar zu verwalten.